from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pyparsing import line
import requests
import json
from rouge import Rouge
from requests.api import get
import os
from docx import Document
import docx
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re

#this url for accessing api
URL = "http://127.0.0.1:8000/summarizerapi/"

# get model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-large")
tokenizer = T5Tokenizer.from_pretrained("t5-large")

# clean html tags
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

#this function convert the file data to text
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# create summarization
def summarization(article):
    input_len = len(article.split())
    # print(input_len)
    spit_input = []
    full_string = []
    output = []

    n = input_len//100

    # print(n)
    s=0
    e=100
    for i in range(n+1):
        spit_input.append(article.split()[s:e])
        full_string.append(' '.join(spit_input[i]))
        e = e + 100
        s = s + 100
    for i in range(n+1):
        # encode the text into tensor of integers using the appropriate tokenizer
        inputs = tokenizer.encode("summarize: " + full_string[i], return_tensors="pt", max_length=100, truncation=True)
        # generate the summarization output
        outputs = model.generate(
            inputs, 
            max_length=100, 
            # min_length=30, 
            length_penalty=2.0, 
            num_beams=4, 
            early_stopping=True)
        output.append(cleanhtml(tokenizer.decode(outputs[0])))

    final_string = ' '.join(output)
    final_string = '. '.join(list(map(lambda x:x.strip().capitalize(),final_string.split("."))))

    return final_string


#This is for homepage
def home(request):
    return render(request, 'base.html')
    
#This is main function where we done everything for summarization
def analyze(request):
    try:
        if request.method == 'POST':
            if request.FILES:
                #this segment for working with file
                rawtext = request.FILES['filename']
                x=getText(rawtext)
                final_reading_time = len(x.split())
                # make summarization
                final_summary = summarization(x)
                summary_reading_time = len(final_summary.split())
                # create validation
                ro = Rouge()
                valuex = ro.get_scores(final_summary,x) 

                mydict = {
                        "mytext":x, 
                        "myword": final_reading_time,
                        "summarize": final_summary,
                        "sumword":summary_reading_time,
                        "valuex": valuex,
                }
                json_data = json.dumps(mydict)
                # request api for post the data
                r = requests.post(url = URL, data=json_data)

                data = r.json()
            else:
                #this segment for working with file
                y=request.POST['text']
                final_reading_time = len(y.split())
                # make summarization
                final_summary = summarization(y)
                summary_reading_time = len(final_summary.split())
                # create validation
                ro = Rouge()
                valuey = ro.get_scores(final_summary,y) 
                mydict = {
                        "mytext":y, 
                        "myword": final_reading_time,
                        "summarize": final_summary,
                        "sumword":summary_reading_time,
                        "valuex": valuey
                }
                json_data = json.dumps(mydict)
                # request api for post the data
                r = requests.post(url = URL, data=json_data)

                data = r.json()
                
        return render(request,'base.html', context=mydict) 
        
    except: 
        return HttpResponse("Opps...!\nSomething else went wrong.")    
            


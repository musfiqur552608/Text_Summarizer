from django.db import models

# Create your models here.
class Summarizer(models.Model):
    mytext = models.CharField(max_length=1000000)
    myword = models.IntegerField()
    summarize = models.CharField(max_length=1000000)
    sumword = models.IntegerField()
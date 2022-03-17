import requests
import json

from requests.api import get

URL = "http://127.0.0.1:8000/summarizerapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)

    data = r.json()

    print(data)

get_data()

# def post_data():
#     data = {
#         'name' : 'Antara Biswas',
#         'roll' : 103,
#         'city' : 'Magura',
#     }

#     json_data = json.dumps(data)
#     r = requests.post(url = URL, data=json_data)

#     data = r.json()

#     print(data)

# # post_data()
# def update_data():
#     data = {
#         'id':3,
#         'name' : 'Jahura Jebin Orin',
#         'city' : 'Dhaka',
#     }

#     json_data = json.dumps(data)
#     r = requests.put(url = URL, data=json_data)

#     data = r.json()

#     print(data)
# #update_data()

def delete_data():
    data = {
        'id':6,
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)

    data = r.json()

    print(data)

#delete_data()
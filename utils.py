from email.policy import default
import os
import requests
from decouple import config

token = config('API_TOKEN', default='')


def postJob(data):
    token = os.environ['ACCESS_TOKEN']
    endpoint = os.environ['API_ENDPOINT']

    try:
        x = requests.post(endpoint, headers={
                          'Authorization': 'Bearer {}'.format(token)}, json=data)
        print(x.json())
    except Exception as error:
        print(error)
        pass

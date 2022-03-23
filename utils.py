from email.policy import default
import os
import requests
from decouple import config

token = config('API_TOKEN', default='')


def postJob(data):
    token = config('ACCESS_TOKEN', default="")
    endpoint = config('API_ENDPOINT', default='')

    try:
        x = requests.post(endpoint, headers={
                          'Authorization': 'Token {}'.format(token)}, json=data)
        x.raise_for_status()
        # print(x.json())
    except Exception as error:
        print(error)
        pass

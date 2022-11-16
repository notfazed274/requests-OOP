import requests
import json


class requestMethods:

    test = 'abc'

    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.payload = payload

    def get(self):
        r = requests.get(self.url)
        return r.status_code

    def get_response(self):
        r = requests.get(self.url)
        return r.json()

    def post(self):
        r = requests.post(self.url, self.headers, self.payload)
        return r.content, r.status_code





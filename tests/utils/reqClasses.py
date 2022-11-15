import json

import requests

class requestMethods:
    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.payload = payload

    url_cat = 'https://http.cat/200'

    def get(self):
        r = requests.get(self.url)
        return r

    def get_response(self):
        r = requests.get(self.url)
        return r.content
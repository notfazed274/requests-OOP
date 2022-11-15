from utils.reqClasses import requestMethods
import json

# Should exclude url from test suite
cats_api = 'https://http.cat/200'

h = open('commonJson.json')
headers = json.load(h)    


def test_get():
    list_of_cats = requestMethods(cats_api,'', '')
    response = list_of_cats.get()
    print(response)

def test_another_get():
    list_of_cats = requestMethods(cats_api, '', '')
    response = list_of_cats.get_response()
    print(response)






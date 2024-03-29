from utils.reqClasses import requestMethods
from utils.endpoints import *
import pytest


def test_api_books_status():
    list_of_books = requestMethods(books_api_list_books, headers, '')
    status_code = list_of_books.get()
    assert status_code == 200
    print(status_code)


def test_api_books_response():
    list_of_books = requestMethods(books_api_list_books, headers, '')
    # response = dict //
    response = list_of_books.get_response()
    print(response[0])


def test_api_books_post():
    list_of_books = requestMethods(books_api_auth, headers, authorization)
    response = list_of_books.post()
    assert response[0] == 200
    print(response)













import json

books_api_status = 'https://simple-books-api.glitch.me/status'
books_api_list_books = 'https://simple-books-api.glitch.me/books'
books_api_auth = 'https://simple-books-api.glitch.me/api-clients'


authorization = json.dumps(
    {
      "clientName": "F",
      "clientEmail": "FP@abc.com"
     }
    )


headers = json.dumps({"Content-Type": "application/json"})


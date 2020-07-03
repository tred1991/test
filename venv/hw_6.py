import requests
import json

# response = urllib.request.urlopen('http://pulse-rest-testing.herokuapp.com/')
# print(response.read())

class FirstScript():
    params = {'id': '50', 'title': 'Second Book', 'author': 'T.Red'}
    r = requests.post('http://pulse-rest-testing.herokuapp.com/books', json=params)
    d = r.json
    id = d["id"]
    print(id)

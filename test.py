import requests
import json

url = 'http://127.0.0.1:5000/add_user'
data = {'name': 'John Doe', 'gender': 'male'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)

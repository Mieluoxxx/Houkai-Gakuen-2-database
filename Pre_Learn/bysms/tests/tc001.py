import pprint
import requests

payload = {
    'username': 'moguw',
    'password': 'moguw123'
}

response = requests.post('http://localhost:8000/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())

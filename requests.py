import json
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://github.com/timeline.json')

print(r.url)
print(r.status_code)
print(r.encoding)
# print(r.headers)
print(r.headers['content-type'])

print("CONTENU AU FORMAT TEXTE")
print(r.text)
# print(r.content)  # contenu binaire
print("CONTENU AU FORMAT JSON")
print(r.json())
print("CONTENU AU FORMAT JSON FORMATE")
print(json.dumps(r.json(), indent=4))

print("EXEMPLE AVEC TOUCAN")
r2 = requests.get('http://localhost:8080/utilisateur/admin',
                  auth=HTTPBasicAuth('admin', 'admin'))
print(r2.status_code)
print(json.dumps(r2.json(), indent=4))

import time
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

start_time = time.time()
r = requests.get('https://github.com/timeline.json')
print("--- %s seconds ---" % (time.time() - start_time))
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
# hostname = 'http://localhost:8080'
hostname = 'https://qftoucanlht01.ad.insee.intra'
session = requests.Session()
# désactivaton proxy
session.trust_env = False
# désactivation SSL
session.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# session.auth = ('admin', 'admin')
token = ''
headers = {'Authorization': 'Bearer ' + token}

start_time = time.time()
# r2 = session.get(hostname + '/utilisateur/admin')
r2 = session.get(hostname + '/utilisateur/njykl1', headers=headers)
print("--- %s seconds ---" % (time.time() - start_time))
print(r2.status_code)
print(r2.json())

data = {"OP": ["OPP2"], "SI": ["SIS10"], "SP": ["SPS0"], "AE": ["AENANN_TOTAL"], "BA": ["BA2014"], "CO": [
    "CONC", "COCE"], "DA": ["DA2016", "DA2017", "DA2018"], "ET": ["ET0"], "PC": ["PCEA", "PCRP"], "CC": ["CCPT0"], "VC": ["VCDEF"]}
r3 = session.post(hostname + '/croisement/tee/search/DOCSNF',
                  headers=headers, json=data)
print(r3.json())

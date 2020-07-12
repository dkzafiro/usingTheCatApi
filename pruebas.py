import requests
import pprint #better format for JSON!
import json

endpoint = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2" 
x = requests.get(endpoint)
datosJson = x.json()
##pprint.pprint(x.json())
text = datosJson[0]['text']
print (text)

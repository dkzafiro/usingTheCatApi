import requests
import pprint #better format for JSON!
import json
##pprint.pprint(r.json())
class getApiRest:
    def getUrl(self):
        endpoint = "https://api.thecatapi.com/v1/images/search?api_key=91dcea0c-fa11-4d35-85f5-a1d2d1508c95"
        r = requests.get(endpoint)
        datosJson = r.json()
        url = datosJson[0]['url']
        return url
    
    def getCatFact(self):
        endpoint = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2" 
        x = requests.get(endpoint)
        datosJson = x.json()
        text = datosJson[0]['text']
        return text
    






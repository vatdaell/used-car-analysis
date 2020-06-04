import json
import urllib
import requests
import pandas as pd

url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List?limit=9999&keys=Make,Model'

with open("keys.json") as f:
    keys = json.load(f)


    headers = {
        'X-Parse-Application-Id': keys["applicationid"], # This is your app's application id
        'X-Parse-REST-API-Key': keys["restapi"] # This is your app's REST API key
    }

data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need

df = pd.DataFrame(data['results'])
df = df[['Make','Model']]
df = df.drop_duplicates()

df.to_csv("carmodels.csv")
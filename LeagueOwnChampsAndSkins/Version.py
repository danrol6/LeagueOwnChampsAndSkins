import requests
import json

url = requests.get("https://EnterYourAPICredentials.leagueoflegends.com/api/versions.json")
text = url.text

data = json.loads(text)

version = data[0]
currentTotalNumberOfChampions = 159
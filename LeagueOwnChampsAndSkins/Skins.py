import json
import requests
import Version
import Champions


#This class gets the skin information for each champion based on the champion list created on the Champions.py class
version = Version.patchVersion
credentials = Version.credentials
champions = Champions.champions

#For each champion, it will fetch its skin information using the champion's ID. Then makes the request and extracts the
#champion's name and their list of skins and adds them to the skins data.
skins = {}
for champion in champions:
    skinURL = requests.get(f"{credentials}/cdn/{version}/data/en_US/champion/{champion}.json")
    skinText = skinURL.text
    skinData = json.loads(skinText)

    championName = skinData['data'][champion]['id']
    championSkins = skinData['data'][champion]['skins']
    skins[championName] = championSkins

print(f"Skins retrieved successfully.")
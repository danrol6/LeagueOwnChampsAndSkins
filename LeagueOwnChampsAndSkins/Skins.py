import json
import requests
import Version
import Champions

version = Version.version
champions = Champions.champions

skins = {}

# print(champions)
for champion in champions:
    url = requests.get(f"http://EnterYourAPICredentials.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champion}.json")
    text = url.text
    data = json.loads(text)

    championName = data['data'][champion]['name']
    championSkins = data['data'][champion]['skins']
    skins[championName] = championSkins

print("Skins retreived successfully.")

#Creating a dictionary for skins

# print((champions['Aatrox']))
print(skins)
print(champions)

print("Appending... ")
champions['Ahri'].append(skins) #appending the new skin data to the current one
#
print("After Appending... ")
print (champions)
print(data)
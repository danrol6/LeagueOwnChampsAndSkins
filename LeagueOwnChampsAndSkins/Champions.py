import Version
import requests
import json

version =  Version.version # Current League version
CtotalChampions = Version.currentTotalNumberOfChampions
print(f"The current version is {version} and the current total number of champions is {CtotalChampions}")

url = requests.get(f"http://[EnterYourAPICredentials].leagueoflegends.com/cdn/{version}/data/en_US/champion.json")
text = url.text

data = json.loads(text)  # parsing to dictionary

champions = list(data['data'].values()) #Gets the list of Champions

champions = {}
for x in data['data'].items():
    # print(x[1])
    champions[x[1]['id']] = [{'key':x[1]['key']}, {'name':x[1]['name']}, {'title':x[1]['title']}]

print("Champions retreived successfully.")
# print(type(champions['Aatrox']))
#
print(f"Total Champions Count: {len(champions)}")

# TO DO FOR THIS PROJECT
# Get a list of all of the champions currently available - DONE
#Get a list of all of the skins - Done
# Save all champions and all skins in a file - Done
# Get images from the URL and save them - Done
# Get a list of all of the champions you currently own
# Get a list of all of the skins for the champion you currently own
# When a champion is selected show whether or not you own that champion and if so what skins you own

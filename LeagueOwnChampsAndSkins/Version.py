import requests
import json
import APICredentials

# Replace "APICredentials.APIURL" with your RIOT Developer Credentials. If needed go to https://developer.riotgames.com/ and sign up for an account.
credentials = APICredentials.APIUrl

# Get current patch version
patchVersionURL = requests.get(f"{credentials}/api/versions.json")
patchText = patchVersionURL.text
patchData = json.loads(patchText)  # Parsing to Dictionary
patchVersion = patchData[0]  # Latest patch Version

# Get Current number of Champions
CTotalNumOfChampsURL = requests.get(f"{credentials}/cdn/{patchVersion}/data/en_US/champion.json")
championText = CTotalNumOfChampsURL.text
championData = json.loads(championText)
champions = list(championData['data'].values())

print(f"The current version is {patchVersion} and the current total number of champions is {len(champions)}")

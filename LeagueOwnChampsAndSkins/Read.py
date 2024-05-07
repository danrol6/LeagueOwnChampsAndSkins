import json

import Write as Write

#Class will read the champions and skins that were written in the Write class
from json.decoder import JSONDecodeError

#Function checks if the json file is empty, or non existent. It returns false if the file is not empty, contains
# valid data and exists
def is_json_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return not bool(data)
    except (FileNotFoundError, JSONDecodeError):
        return True


if is_json_empty('skins.json'):
    print("skins.json is empty, contains invalid JSON data or does not exists. Calling the Write class...")
    Write()
    print("...Write class called")

print("importing skins...")
fskins = open('skins.json')
skins = json.load(fskins)
fskins.close()
print("...Imported successfully")

if is_json_empty('champions.json'):
    print("skins.json is empty, contains invalid JSON data or does not exists. Calling the Write class...")
    Write()
    print("...Write class called")

print("importing champions...")
fchampions = open('champions.json')
champions = json.load(fchampions)
fchampions.close()
print("...Imported successfully")
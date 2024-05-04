import json

print("importing skins...")
fskins = open('skins.json')
skins = json.load(fskins)
fskins.close()
print("...Imported successfully")

print("importing champions...")
fchampions = open('champions.json')
champions = json.load(fchampions)
fchampions.close()
print("...Imported successfully")
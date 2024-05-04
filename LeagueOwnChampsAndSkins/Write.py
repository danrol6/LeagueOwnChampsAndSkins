import Version
import Champions
import Skins
import json

champions = Champions.champions
skins = Skins.skins

print("Writing champions to file...")
champWrite = json.dumps(champions)

f = open("champions.json", "w")

f.write(champWrite)

f.close()
print("...Champions successfully written!")

print("Writing skins to file...")
skinWrite = json.dumps(skins)

f = open("skins.json", "w")

f.write(skinWrite)

f.close()
print("...Skins successfully written!")
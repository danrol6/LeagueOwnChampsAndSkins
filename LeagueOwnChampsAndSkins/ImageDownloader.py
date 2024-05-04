import os.path
import urllib.request
from pathlib import Path
import Read

skins = Read.skins

# print(skins['Aatrox'][1]['num'])
# print((skins['Aatrox'][1]))


print(len(skins))
for champ in skins:
    print(champ)
    for skin in skins[champ]:
        print(skin['num'], end=" ")
        print(skin['name'])
        Path(f"ChampionImages/{champ}").mkdir(parents=True, exist_ok=True)
        if not (os.path.isfile(f"ChampionImages/{champ}/{champ}_{skin['num']}.jpg")):
            print(f"{champ}_{skin['num']}.jpg Does not exist... Downloading Image...")
            urllib.request.urlretrieve(
                f"http://EnterYourAPICredentials.leagueoflegends.com/cdn/img/champion/splash/{champ}_{skin['num']}.jpg",
                f"ChampionImages/{champ}/{champ}_{skin['num']}.jpg")
    

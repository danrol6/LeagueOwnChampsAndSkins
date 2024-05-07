import os.path
import urllib.error
from pathlib import Path
import Read
import Version

#This class downloads the image of the skin based on the champions name and stores it on the respective folder.
credentials = Version.credentials
skins = Read.skins
champions = Read.champions

#The loop iterates through each champion and checks for its key which is then use to look up the skin associated with
# that key. If the image does not exists locally it connects to the API and downloads it. If an error occurs while
# downloading an image, it generates and error and continues downloading the rest of the images. If the image already
# exists locally it will print a message saying so
for champion, champion_data in champions.items():
    champion_id = None
    for data in champion_data:
        if 'key' in data:
            champion_id = data['key']
            break

    if champion_id:
        skins_data = skins.get(champion)
        if skins_data:
            for skin in skins_data:
                skin_id = skin['id']
                num = skin['num']
                path = f"ChampionImages/{champion}"
                Path(path).mkdir(parents=True, exist_ok=True)
                if not (os.path.isfile(f"ChampionImages/{champion}/{champion}_{num}.jpg")):
                    print(f"{champion}_{num}.jpg Does not exist... Downloading Image...")
                    try:
                        urllib.request.urlretrieve(
                            f"{credentials}/cdn/img/champion/splash/{champion}_{num}.jpg",
                            f"ChampionImages/{champion}/{champion}_{num}.jpg")
                    except urllib.error.HTTPError as e:
                        if e.code == 403:
                            print(f"Access to {champion}_{num}.jpg is forbidden.")
                        else:
                            print(f"Failed to download {champion}_{num}.jpg: {e}")
                    except Exception as e:
                        print(f"An error occurred while downloading {champion}_{num}.jpg: {e}")
                else:
                    print(f"{champion}_{num}.jpg already exists.")

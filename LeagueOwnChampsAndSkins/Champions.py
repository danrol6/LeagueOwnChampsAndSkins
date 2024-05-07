import Version

#This class gets the data from each champion
championData = Version.championData

#Itirates through the champions and stores only the Champion Key, Name, and Title. The Champion ID is the key
champions = {}
for x in championData['data'].items():
    champions[x[1]['id']] = [{'key':x[1]['key']}, {'name':x[1]['name']}, {'title':x[1]['title']}]

print("Champions retreived successfully.")

print(f"Total Champions Count: {len(champions)}")

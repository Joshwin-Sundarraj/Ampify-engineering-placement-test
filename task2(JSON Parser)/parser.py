import urllib.request as u
import json as j

url = "https://api.ampifymusic.com/packs "

response = u.urlopen(url)
data = j.loads(response.read())
data = data['packs']

def myFunc(e):
    return e['genres']
data.sort(key=myFunc)

genres = list(set([each['genres'][0] for each in data]))
genres.sort()
d = {each:[] for each in genres}

i = 0
j = 0
while i < len(data):
    if data[i]['genres'][0]== genres[j]:
        d[genres[j]].append(data[i])
    else:
        j+=1
        continue
    i +=1

print("List of all genres:\n",genres)

print("\nList of all packs in the hip-hop genre:")
for each in d['hip-hop']:
  print(each)
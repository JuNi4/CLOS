from textwrap import indent
import requests
import json
import time

print('')
print(' ___   ___   ___  ____  __  ___  ____')
print(' |  |  |  |  |  | |__| |  | | |  |__|')
print(' |  |  |  |  |  | ____ |  |_| |  ____')
print(' |  |  |  |  |  | |  | |  |___|  |  |')
print(' |  |  |  |  |  | |  | |  |_ |   |  |')
print(' |  |__|  |__|  | |  | |  | | |  |  |')
print(' |______________| |__| |__| |_|  |__|')
print('    ')
print(' Please Input Term to Search')
st = input('>>>')

rq = requests.get('https://de.wikipedia.org/wiki/'+st)
j = json.loads(str(rq.json()))
f = open('wiki_request.json','w')
f.write(json.dumps(j,indent=4))
f.close()
print('lol')
# LOL
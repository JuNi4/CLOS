from textwrap import indent
import requests
import json
import time

import wikipedia

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
st = input('>>> ')

try:
    if wikipedia.suggest(st).lower() != st.lower():
        print('Did you mean: ' + wikipedia.suggest(st)+'? (y/n)')
        a_sugestion = input('>>> ')
        if a_sugestion.lower() == 'y':
            st = wikipedia.suggest(st)
except:
    pass

rq = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search='+st)
sresult = json.loads(rq.text)
c = 0
for o in sresult[1]:
    c += 1
    print(' '+str(c)+'. '+o)
print('Please select one Between 1 and '+str(len(sresult[1])))
p = input('>> ')
if not int(p) in range(1,len(sresult[1])):
    print('Invalid Selection')
    exit()

print('Showing summary of '+sresult[1][int(p)-1]+'\n')

print(wikipedia.summary(sresult[1][int(p)-1]))
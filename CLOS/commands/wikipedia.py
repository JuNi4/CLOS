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

rq = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search='+st)
sresult = json.loads(rq.text)
c = 0
for o in sresult[1]:
    c += 1
    print(' '+str(c)+'. '+o)
print('Please select one Between 1 and '+str(len(sresult[1])+1))
p = input('>>')
if not p in range(1,len(sresult[1])):
    exit()
rq = requests.get('https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+sresult[1][int(p)-1])
print(rq.text)
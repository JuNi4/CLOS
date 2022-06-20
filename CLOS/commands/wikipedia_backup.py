from textwrap import indent
import requests
import json
import time

def jsonstr_to_str(jsonstr, title = 'none', textbody = '*ignored!', subbody = 'none', allow_underlined = False, allow_newlines = True):
    # Setting Vallues
    x = ""
    y = ""
    js = jsonstr
    if not subbody == 'none':
        js = json.loads(js)[subbody]
    if not title == 'none':
        y = json.loads(js)[title]
    if not textbody == '*ignored!':
        js = json.loads(js)[textbody]
    # Actual Formatting
    if allow_underlined:
        js.replace('==', '')
    else:
        js.replace('==', '')
    if allow_newlines:
        js.replace('\\n', '\n')
    else:
        js.replace('\\n','')
    x = js
    return [y,x]

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
print('Please select one Between 1 and '+str(len(sresult[1])))
p = input('>>')
if not int(p) in range(1,len(sresult[1])):
    exit()
rq = requests.get('https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&page='+sresult[1][int(p)-1])
content = json.loads(rq.text)
print(jsonstr_to_str(rq.text)[1], 'title','wikitext','parse')
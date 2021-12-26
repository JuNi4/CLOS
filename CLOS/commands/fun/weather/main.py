import requests
import json

addr = "http://api.openweathermap.org/data/2.5/weather?q=Ilsede&appid={0[0]}"
api = ["a85e9bca9503b1586b8cc8722c8a6c19", "Citty"]
#ips = requests.get('https://ipinfo.io/loc').text
#ip = format(ips)
#locr = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
#loc = json.loads(json.dumps(locr))
#api[1] = loc['city']
r = requests.get(addr.format(api))
weather = json.loads(str(r.text))
weath = json.loads(json.dumps(weather["weather"][0]))
wind = json.loads(json.dumps(weather["wind"]))
temp = json.loads(json.dumps(weather["main"]))
print('Weather: '+weath["main"])
print('Description: '+weath["description"])
print('Windspeed: '+str(wind["speed"]))
print('Wind direction: '+str(wind["deg"])+'°')
print(r.text)
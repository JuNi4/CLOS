import requests
import pathlib
import json

# Function for only showing two numbers after decimal point    This accepts string and float
def declimit(number,declim,decdot = '.',replace=''):
    # Number type
    nt = str(type(number))
    # function to check if the number even has a decimal dot like if it is an int and not float or its a custom decimal point
    if not decdot in str(number): return
    # if the decimal dot should be replaced with the replace var
    if not replace == '':
        number = str(number).replace(decdot, replace)
        decdot = replace
    # String the number
    str(number)
    # get declim amount of decimal numbers
    number = number.split(decdot)[0]+decdot+number.split(decdot)[1][:declim]
    # if number was float, return float
    if 'float' in nt:
        return float(number)
    # else return string
    return number
    
# API web address
addr = "https://api.openweathermap.org/data/2.5/weather?q=Ilsede&appid={0[0]}"
# api key and Cittyplaceholder
# The API key you cab get from https://openweathermap.org/api wich is free, has to be pasted into the weatherapi.txt file that needs to go into the command_data folder
if not pathlib.Path()
api = [, "Citty"]
#ips = requests.get('https://ipinfo.io/loc').text
#ip = format(ips)
#locr = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
#loc = json.loads(json.dumps(locr))
#api[1] = loc['city']
# get weather data from api
r = requests.get(addr.format(api))
# get weather list from response
weather = json.loads(str(r.text))
weath = json.loads(json.dumps(weather["weather"][0]))
# get wind data from response
wind = json.loads(json.dumps(weather["wind"]))
# get temp data from response
temp = json.loads(json.dumps(weather["main"]))
# Display data
print('Weather: '+weath["main"])
print('Description: '+weath["description"])
print('Windspeed: '+str(wind["speed"]))
print('Wind direction: '+str(wind["deg"])+'°')
print('Temperatur: '+declimit(str(temp["temp"]-273.15),2)+'°C')
print('Feels like: '+declimit(str(temp["feels_like"]-273.15),2)+'°C')
print('Minimum: '+declimit(str(temp["temp_min"]-273.15),2)+'°C, Maximum: '+declimit(str(temp["temp_max"]-273.15),2)+'°C')
#print(r.text)
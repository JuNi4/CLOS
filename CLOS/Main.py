# Main Command Line Operating System (CLOS) File
# Import Stuff
print('Info: Importing Important Libs...', end='\r')
import os
import sys
import time
import json
import platform
print('Info: Importing Important Libs... Done!')

boot_start = time.time()
f = open(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json')
boot_opt = json.loads(json.dumps(f.read()))
f.close()

# Import Color
print('Info: Importing Libs From Libs Folder...', end='\r')
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'\libs\\')
import color as style
info_style = style.color.Blue
warning_style = style.color.Yellow
error_style = style.color.Red
res = style.color.Default + style.backcolor.BackgroundDefault
print(info_style+'Info: Importing Libs From Libs Folder... Done!'+res)

# Install Stuff
if 'Windows' in platform.system():
    print(info_style+'Info: Downloading Libs...'+res,end='\r')
    os.system('pip install requests>nil')
    os.system('pip install pythonping>nil')
    os.system('pip install urllib3>nil')
    print(info_style+'Info: Downloading Libs... Done!'+res)

# Import More Stuff
print(info_style+'Info: Importing More Libs...'+res,end='\r')
from urllib3.packages.six import _MovedItems
import http.client as httplib
from pythonping import ping
from pathlib import Path
import requests
print(info_style+'Info: Importing More Libs... Done!'+res)

# Set Title
os.system('title CLOS (Command Line Operating System)')

# Commands
clear = lambda: os.system('cls')
ie = 0

# Check for Internet
def internet():
    if ie == 1:
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False
    else:
        return False

# Vars
skip_setup = 0
print(info_style+'Info: Checking For Internet... If Crashes, Disable Internet In Boot Settings.'+res,end='\r')
if internet() == True:
    ips = requests.get('https://api.ipify.org').text
    ip = format(ips)
    locr = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
else:
    locr = {'country_code': 'US', 'country_name': 'Germany', 'city': 'Tuerkenfeld', 'postal': '82299', 'latitude': 48.1053, 'longitude': 11.083, 'IPv4': '94.31.96.202', 'state': 'Bavaria'}
print(info_style+'Info: Checking For Internet... Done! If Crashes, Disable Internet In Boot Settings.'+res)
template = {
    "setup": "done",
    "name": "none",
    "fav_food": "none",
    "fav_color": "none",
    "lan": "en_us",
    "scheme": "dark"
}
lan_template = {
    "setting_found": "Info: Found Settings file",
    "setting_missing": "Error: Settings file not existant!",
    "setting_creat": "Info: Creating Settings file",

    "y": "y",
    "n": "n",

    "su_laun": "Launching setup...",
    "su_lan_rq": "Please select a language:",
    "su_name_rq": "Please input your name:",
    "su_lan_change_rq": "Do you want to change your current language? Y/N",
    "su_cur_lan": "Currently ",
    "su_fav_food_rq": "Please input your favorite food:",
    "su_fav_color": "Please input your favorite color:",
    "su_fav_color_av": "Available are 'Red', 'Green', 'Blue', 'Yellow', 'Magenta', 'Cyan'",

    "wm_welcome": "Welcome ",
    "wm_p1": " to Command Line Operating System (CLOS).",
    "wm_p2": "You can turn of this Message using the 'settings' command."
}
temp = json.loads(json.dumps(template))
loc = json.loads(json.dumps(locr))
if loc['country_code'] == 'DE':
    temp["lan"] = "de_de"
elif loc['country_code'] == 'US':
    temp["lan"] = "en_us"
else:
    temp["lan"] = "en_us"

# Setup 
def setup(fp):
    # Load lan
    lann = temp["lan"]
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '\lan\\' + lann + '.json')
    lf = open(lan_file, 'r')
    lan = json.loads(lf.read())
    lf.close()
    # Lan rq
    print(lan["su_laun"])
    time.sleep(2)
    print(lan["su_lan_change_rq"])
    x = input()
    if x.lower() == lan["y"]:
        print(lan["su_lan_rq"])
        print('- en_us')
        print('- de_de')
        temp["lan"] = input().lower()
    # Load lan again
    lann = temp["lan"]
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '\lan\\' + lann + '.json')
    lf = open(lan_file, 'r')
    lan = json.loads(lf.read())
    lf.close()
    # Name rq
    print(lan["su_name_rq"])
    temp["name"] = input()
    # Fav Food rq
    print(lan["su_fav_food_rq"])
    temp["fav_food"] = input()
    # Fav Color rq
    print(lan["su_fav_color"])
    print(lan["su_fav_color_av"])
    temp["fav_color"] = input().lower()
    # Color Scheme rq
    print('Please select a Theme:')
    print('light / dark')
    temp["scheme"] = input().lower()
    if temp["scheme"]=="light": 
        print(style.backcolor.BackgroundWhite + style.color.Black)
    else:
        print(style.backcolor.BackgroundDefault + style.color.Default)
    # Write Settings
    set = json.dumps(temp, indent=4)
    sf = open(fp, 'w')
    sf.write(set)
    sf.close()

# Functions
def command(command):
    command2 = requests.findall('"([^"]*)"', command)
    if ' ' in command:
        command1 = str(command).split()
        commandf = command1[0]
        x = command[len(commandf):]
        if '"' in command:
            command2 = requests.findall('"([^"]*)"', command)
        else:
            command2 = [command, command]
        if commandf in command2[0]:
            commandf = command
            x = ''
    else:
        commandf = command
        x = ''
    fc = os.path.dirname(os.path.realpath(__file__)) + '\commands\\' + commandf + '.py'
    fp = os.getcwd() + '\\' + commandf
    my_file = Path(fc)
    if my_file.is_file():
        os.system(str(fc) + x)
    else:
        my_file = Path(fp)
        if my_file.is_file():
            os.system(commandf + x)
        else:
            print('No File or Command found caled ' + commandf+ '. Use the \'help\' command for a list of all available commands.')

def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

# Load settings
fp = os.path.dirname(os.path.realpath(__file__))  + '\data\settings.json'
settings_filep = Path(fp)
if settings_filep.is_file():
    settings_file = open(fp, 'r')
    settings = json.loads(settings_file.read())
    settings_file.close()
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '\lan\\' + settings["lan"] + '.json')
    lan_path = Path(os.path.dirname(os.path.realpath(__file__)) + '\lan')
    if not lan_file.is_file():
        #Language
        if not lan_path.is_dir():
            os.system('mkdir ' + os.path.dirname(os.path.realpath(__file__)) + '\lan\\')
        lan_usf = os.path.dirname(os.path.realpath(__file__)) + '\lan' + '\en_us.json'
        lan_f_en_us = open(lan_usf, 'w')
        lan_f_en_us.write(lan_template)
        lan_f_en_us.close()
        settings["lan"] = "en_us"
    lan_f = open(lan_file, 'r')
    lan = json.loads(lan_f.read())
    lan_f.close()
    print(info_style+lan["setting_found"]+res)
else:
    lan = lan_template
    print(error_style+lan["setting_missing"]+res)
    print(info_style+lan["setting_creat"]+res)
    if skip_setup == 0:
        setup(fp)
    else:
        f = open(fp, 'w')
        f.write(json.dumps(template, indent=4))
        f.close()
    settings_file = open(fp, 'r')
    settings = json.loads(settings_file.read())
    settings_file.close()
    settings["lan"] = temp["lan"]
time.sleep(2)
if settings["setup"]=="not_done":
    setup(fp)

# Welcomscreen
settings_file = open(fp, 'r')
settings = json.loads(settings_file.read())
settings_file.close()

lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '\lan\\' + settings["lan"] + '.json')
lan_f = open(lan_file, 'r')
lan = json.loads(lan_f.read())
lan_f.close()
boot_end = time.time()
boot_time1= boot_end - boot_start
boot_time = str(boot_time1)[:4]
print(info_style+'Info: Booting Done! Took '+str(boot_time)+' s.'+res)
if settings["scheme"]=="light": 
    print(style.backcolor.BackgroundWhite + style.color.Black)
else:
    print(style.backcolor.BackgroundDefault + style.color.Default)
print(lan["wm_welcome"] + str(settings["name"]) + lan["wm_p1"])
print(lan["wm_p2"])

# Space...
print('')

# Input
while True:
    inp = str(input(os.getcwd()+'>')).lower()
    if inp == 'redo_setup':
        setup(fp)
    elif inp == 'exit':
        exit()
    elif inp == 'shutdown':
        exit()
    elif inp == 'reboot':
        exit()
    elif inp == 'sys':
        print('CLOS (Command Line Operating Sysrem)')
    elif inp == '':
        print('nput needed')
    elif inp[:6] == 'python':
        if 'python ' in inp:
            os.system('python -c "'+inp[7:]+'"')
        else:
            os.system('python')
    elif 'internet' in inp:
        if internet() == True:
            if 'internet ' in inp:
                response_list = ping('google.com', size=40, count=int(inp[9:]))
            else:
                response_list = ping('google.com', size=40, count=4)
            ms = str(response_list.rtt_avg_ms)
            print('Currently Your Connected To The Internet With A Ping Of '+ms+'ms.')
        else:
            print('Currently There Is No Connection With The Internet.')
    else:
        command(inp)
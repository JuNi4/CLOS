# Main Command Line Operating System (CLOS) File # Änderung Nr. 4 14.8.2021 21:00
# Import Stuff
print('Info: Importing Important Libs...', end='\r')
import os
import sys
import time
import json
import platform
from pathlib import Path

boot_start = time.time()

print('Info: Importing Important Libs... Done!')

if 'Windows' in platform.system():
    boot_file = Path(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json')
else:
    boot_file = Path(os.path.dirname(os.path.realpath(__file__))+'/data/boot_opt.json')
if boot_file.is_file():
    if 'Windows' in platform.system():
        f = open(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json', 'r')
    else:
        f = open(os.path.dirname(os.path.realpath(__file__))+'/data/boot_opt.json', 'r')
    boot_opt = json.loads(f.read())
    f.close()
else:
    boot_options_template = {
    "internet_con": "true",
    "default_lan": "en_us",
    "color_enabled": True,
    "install_libs": True,
    "time_wait_after_startup": 2,
    "vancy_prompt": False
    }
    if 'Windows' in platform.system():
        f = open(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json', 'w')
    else:
        f = open(os.path.dirname(os.path.realpath(__file__))+'/data/boot_opt.json', 'w')
    f.write(json.dumps(boot_options_template,indent=4))
    f.close()
    if 'Windows' in platform.system():
        f = open(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json', 'r')
    else:
        f = open(os.path.dirname(os.path.realpath(__file__))+'/data/boot_opt.json', 'r')
    boot_opt = json.loads(f.read())
    f.close()


# Import Color
print('Info: Importing Libs From Libs Folder...', end='\r')
if 'Windows' in platform.system():
    sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/libs/')
else:
    sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/libs/')
import clos_utils as cutil
import vars
style = cutil.text_style
info_style = style.color.Blue
warning_style = style.color.Yellow
error_style = style.color.Red
res = style.color.Default + style.backcolor.Default
print(cutil.utils.ifcolor('Info: Importing Libs From Libs Folder... Done!',info_style,res))

# Install Stuff
if boot_opt["install_libs"]:
    print(cutil.utils.ifcolor('Info: Downloading Libs...',info_style,res),end='\r')
    if 'Windows' in platform.system():
        os.system('pip install requests>nil')
        os.system('pip install pythonping>nil')
        os.system('pip install urllib3>nil')
    else:
        os.system('pip3 install requests>nil')
        os.system('pip3 install pythonping>nil')
        os.system('pip3 install urllib3>nil')
    print(cutil.utils.ifcolor('Info: Downloading Libs... Done!',info_style,res))
    boot_opt["install_libs"] = False
    if 'Windows' in platform.system():
        f = open(os.path.dirname(os.path.realpath(__file__))+'\\data\\boot_opt.json', 'w')
    else:
        f = open(os.path.dirname(os.path.realpath(__file__))+'/data/boot_opt.json', 'w')
    f.write(json.dumps(boot_opt,indent=4))
    f.close()

# Import More Stuff
print(cutil.utils.ifcolor('Info: Importing More Libs...',info_style,res),end='\r')
if 'Windows' in platform.system():
    from urllib3.packages.six import _MovedItems
import http.client as httplib
from pythonping import ping
import requests
import getpass
print(cutil.utils.ifcolor('Info: Importing More Libs... Done!',info_style,res))

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
do_setup = False
skip_setup = 0
dir_temp = json.loads(json.dumps(vars.dir_template))
if 'Windows' in platform.system():
    dir_temp["CLOS_DIR"] = str(os.path.dirname(os.path.realpath(__file__)))
    dir_temp["LIB_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\libs'
    dir_temp["COMMAND_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\commands'
    dir_temp["COMMAND_DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\command_data'
    dir_temp["DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\data'
    dir_temp["COMMAND_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\commands'
    dir_temp["COMMAND_DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\command_data'
    dir_temp["DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\data'
    dir_temp["LAN_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '\lan'
else:
    dir_temp["CLOS_DIR"] = str(os.path.dirname(os.path.realpath(__file__)))
    dir_temp["LIB_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/libs'
    dir_temp["COMMAND_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/commands'
    dir_temp["COMMAND_DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/command_data'
    dir_temp["DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/data'
    dir_temp["COMMAND_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/commands'
    dir_temp["COMMAND_DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/command_data'
    dir_temp["DATA_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/data'
    dir_temp["LAN_DIR"] = str(os.path.dirname(os.path.realpath(__file__))) + '/lan'
if 'Windows' in platform.system():
    dirf = open(str(os.path.dirname(os.path.realpath(__file__)))+'\libs\dirs.json', 'w')
else:
    dirf = open(str(os.path.dirname(os.path.realpath(__file__))) + '/libs/dirs.json', 'w')
dirf.write(json.dumps(dir_temp, indent=4))
dirf.close()
if 'Windows' in platform.system():
    dirf = open(str(os.path.dirname(os.path.realpath(__file__)))+'\commands\dirs.json', 'w')
else:
    dirf = open(str(os.path.dirname(os.path.realpath(__file__))) + '/commands/dirs.json', 'w')
dirf.write(json.dumps(dir_temp, indent=4))
dirf.close()
print(cutil.utils.ifcolor('Info: Checking For Internet... If Crashes, Disable Internet In Boot Settings.',info_style,res),end='\r')
if internet() == True:
    ips = requests.get('https://api.ipify.org').text
    ip = format(ips)
    locr = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
else:
    locr = {'country_code': 'US', 'country_name': 'Germany', 'city': 'Tuerkenfeld', 'postal': '82299', 'latitude': 48.1053, 'longitude': 11.083, 'IPv4': '94.31.96.202', 'state': 'Bavaria'}
print(cutil.utils.ifcolor('Info: Checking For Internet... Done! If Crashes, Disable Internet In Boot Settings.',info_style,res))
template_pata = vars.template_pata
template = vars.template
lan_template = vars.lan_template
temp_pata = json.loads(json.dumps(template_pata))
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
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '/lan/' + lann + '.json')
    lf = open(lan_file, 'r')
    lan = json.loads(lf.read())
    lf.close()
    # Lan rq
    print(lan["su_laun"])
    time.sleep(2)
    print(lan["su_lan_change_rq"])
    x = input()
    if x.lower() == lan["y"]:
        def lan_request(lan):
            known_lans = ['de_de','en_us']
            print(lan["su_lan_rq"])
            lan_files = cutil.utils.getObjectinFolder(os.path.dirname(os.path.realpath(__file__)) + '/lan', blacklist = ["dirs.json"])
            no_end = []
            for object in lan_files:
                index = lan_files.index(object)
                object = object.split('.')[0]
                no_end.append(object)
                if object in known_lans:
                    if object == settings["lan"]:
                        print(str(index+1)+'. -> '+lan["lan_"+object])
                    else:
                        print(str(index+1)+'. - '+lan["lan_"+object])
                else:
                    if object == settings["lan"]:
                        print(str(index+1)+'. -> '+object)
                    else:
                        print(str(index+1)+'. - '+object)
            inp_lan = input().lower()
            if inp_lan == lan["lan_de_de"]:
                temp = 'de_de'
            elif inp_lan == lan["lan_en_us"]:
                temp = 'en_us'
            elif inp_lan == lan["lan_en_uk"]:
                temp = 'en_uk'
            elif inp_lan in no_end:
                temp = inp_lan
            elif 0 <= int(inp_lan) - 1 <= len(lan_files)-1:
                temp = no_end[int(inp_lan)-1]
            else:
                temp = lan_request(lan)
            return temp
        temp["lan"] = lan_request(lan)
        #temp["lan"] = 
    # Load lan again
    lann = temp["lan"]
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '/lan/' + lann + '.json')
    lf = open(lan_file, 'r')
    lan = json.loads(lf.read())
    lf.close()
    # Name rq
    print(lan["su_name_rq"])
    temp["name"] = input()
    # PW rw
    print(lan["su_pw_rq"])
    temp_pata["admin_pw"] = getpass.getpass(prompt='')
    print('*'*len(str(temp_pata["admin_pw"])))
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
        print(style.backcolor.White + style.color.Black)
    else:
        print(style.backcolor.Default + style.color.Default)
    # Write Settings
    set = json.dumps(temp, indent=4)
    sf = open(fp, 'w')
    sf.write(set)
    sf.close()
    set = json.dumps(temp_pata, indent=4)
    if 'Windows' in platform.system():
        sf = open(str(privat_f)+'\data_clos.json', 'w')
    else:
        sf = open(str(privat_f) + '/data_clos.json', 'w')
    sf.write(set)
    sf.close()

# Functions



# Load settings
print(cutil.utils.ifcolor('Info: Creating Files...',info_style,res),end='\r')
fp = os.path.dirname(os.path.realpath(__file__))  + '/data/settings.json'
settings_filep = Path(fp)
privat_f = Path(os.path.dirname(os.path.realpath(__file__)) + '/private_data')
if 'Windows' in platform.system():
    if not privat_f.is_dir():
        os.system('md "'+str(privat_f)+'"')
    os.system('attrib +h +s "'+str(privat_f)+'"')
else:
    if not privat_f.is_dir():
        os.system('mkdir "'+str(privat_f)+'"')
if settings_filep.is_file():
    settings_file = open(fp, 'r')
    settings = json.loads(settings_file.read())
    settings_file.close()
    lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '/lan/' + settings["lan"] + '.json')
    lan_path = Path(os.path.dirname(os.path.realpath(__file__)) + '/lan')
    if not lan_file.is_file():
        #Language
        if not lan_path.is_dir():
            os.system('mkdir ' + os.path.dirname(os.path.realpath(__file__)) + '/lan/')
        lan_usf = os.path.dirname(os.path.realpath(__file__)) + '/lan' + '/en_us.json'
        lan_f_en_us = open(lan_usf, 'w')
        lan_f_en_us.write(lan_template)
        lan_f_en_us.close()
        settings["lan"] = "en_us"
    lan_f = open(lan_file, 'r')
    lan = json.loads(lan_f.read())
    lan_f.close()
    print(cutil.utils.ifcolor('Info: Creating Files... Done!',info_style,res))
    print(cutil.utils.ifcolor(lan["setting_found"],info_style,res))
else:
    lan = lan_template
    settings = json.loads(json.dumps(template))
    print(cutil.utils.ifcolor('Info: Creating Files... Done!',info_style,res))
    print(cutil.utils.ifcolor(lan["setting_missing"],error_style,res))
    print(cutil.utils.ifcolor(lan["setting_creat"],info_style,res))
    if skip_setup == 0:
        do_setup = True
        boot_end = time.time()
        setup(fp)
    else:
        f = open(fp, 'w')
        f.write(json.dumps(template, indent=4))
        f.close()
    settings_file = open(fp, 'r')
    settings = json.loads(settings_file.read())
    settings_file.close()
    settings["lan"] = temp["lan"]
time.sleep(boot_opt["time_wait_after_startup"])
if settings["setup"]=="not_done":
    do_setup = True
    boot_end = time.time()
    setup(fp)

# Welcomscreen
settings_file = open(fp, 'r')
settings = json.loads(settings_file.read())
settings_file.close()

lan_file = Path(os.path.dirname(os.path.realpath(__file__)) + '/lan/' + settings["lan"] + '.json')
lan_f = open(lan_file, 'r')
lan = json.loads(lan_f.read())
lan_f.close()
if not do_setup:
    boot_end = time.time()
boot_time1= boot_end - boot_start
boot_time = str(boot_time1)[:4]
print(cutil.utils.ifcolor('Info: Booting Done! Took '+str(boot_time)+' s.',info_style,res))
if settings["scheme"]=="light": 
    print(style.backcolor.White + style.color.Black)
else:
    print(style.backcolor.Default + style.color.Default)
print(lan["wm_welcome"] + str(settings["name"]) + lan["wm_p1"])
print(lan["wm_p2"])

# Space...
print('')

# Input
while True:
    if boot_opt["vancy_prompt"]:
        # Displays A Fancy prompt using oh-my-posh. Needs to be installed. (Under windows just type this into the command prompt: 'winget install JanDeDobbeleer.OhMyPosh') Offical Website: https://ohmyposh.dev
        inp = str(input(str(os.system('oh-my-posh --config '+os.path.dirname(os.path.realpath(__file__))+boot_opt["vancy_prompt_opt_rel_path"]))[:os.system('oh-my-posh --config '+os.path.dirname(os.path.realpath(__file__))+boot_opt["vancy_prompt_opt_rel_path"]+'>nil')])).lower()
    else:
        inp = str(input(os.getcwd()+'>')).lower()
    if inp == 'redo_setup':
        setup(fp)
    if inp == 'setup':
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
        cutil.commands.command(command = inp)
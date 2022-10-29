# CLOS Installer; Creddits: JuNi4; github.com/JuNi4

import clos_console_menu as cmenu
import os

# Make Sure You want to install
start = cmenu.prompt('CLOS Installer', 'You are about to "install" CLOS. Do you wish to continue?')
if start == 0:
    exit(0)
# License Agreement
lagree = cmenu.prompt('CLOS Installer', 'License Agreement: Do NOT steal, feel   free to modify, suggest fetures and     report Bugs. I Hate Bugs!', abut='Decline', bbut='Accept')
if lagree == 0:
    exit()
# Language Strings
german = ['Deutsch','Die Deutsche Sprache.','Bitte wählen sie eine Sprache aus:','Sind sie sicher, dass sie die Sprache   "','" nutzen wollen?','OK','Abbrechen', 'Bitte geben sie Namen und Password ein:','Name    ','Passwort','Dein Account Name für CLOS','Dein Admin Passwort (fürs ausführen von manchen Apps)','Bitte wähle Commandpackete aus:','Benötigt','Werkzeuge','Spaß','Grundlegende und Benötigte Commands für grundlegende Aufgaben','Nützliche Werkzeuge, werden nicht benötigt.','Lusstige Commands, die eher zum Spaß gedacht sind. Wie einen Donut.']
english =['English (US)','The English language that is found in   the USA.','Please select a language:','Are you sure you want to use the        language "','"?', 'OK','Cancle','Please input A name and A password','Name    ','Password','Your Account name for CLOS','You Admin password (for executing some  Apps)','Please select Command packets to install:','Required','Tools','Fun','The Required Commands to do the most basic commands.','Tools that are usefull but not needed.','Fun Commands like spinning Donuts']
lans = [english,german]
lan_list = []
lan_desc = []
# Language Selection
s = 0
lan = 0
for o in lans:
    lan_list.append(o[0])
    lan_desc.append(o[1])
while s == 0:
    lan = cmenu.styl_menu_vert('CLOS Installer',prompt =lans[lan][2], entrys=lan_list, description=lan_desc)
    lan2 = lans[lan][0]
    s = cmenu.prompt('CLOS Installer', lans[lan][3]+lan2+lans[lan][4], abut=lans[lan][6],bbut=lans[lan][5])
# Name And Password input
cmenu.custom_input_menu('CLOS Installer',prompt=lans[0][7],entrys=[lans[0][8],lans[0][9]],description=[lans[lan][10],lans[lan][11]],default_vals=[os.getlogin()])
# Select Command packages to be installed
cmenu.styl_menu_vert_mult('CLOS Installer',prompt=lans[lan][12],entrys=[lans[lan][13],lans[lan][14],lans[lan][15]],description=[lans[lan][16],lans[lan][17],lans[lan][18]])

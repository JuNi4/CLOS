# This is going to be my own NOT LINUX ONLY console menu. In python.
import keyboard
import time
import os

# One that supports fixed amount of entys:
def basic_menu():
    sel = 1
    oentry1 = ' 1 - Hello'
    oentry2 = ' 2 - Hallo'
    entry1 = oentry1
    entry2 = oentry2
    done = False
    while not done:
        if sel > 2:
            sel = 1
        if sel < 1:
            sel = 2
        if sel == 1:
            entry1 ='> '+oentry1+' <'
        else:
            entry1 = ' '+oentry1
        if sel == 2:
            entry2 ='> '+oentry2+' <'
        else:
            entry2 = ' '+oentry2
        print('====================================\nMenu_Title\n====================================\n'+entry1+'\n'+entry2)
        keyboard.read_key()
        if keyboard.is_pressed('nach-unten'):
            sel += 1
        if keyboard.is_pressed('nach-oben'):
            sel -= 1
        if keyboard.is_pressed('enter'):
            done = True
            return sel
        os.system('cls')

#basic_menu()

# Stylised slection menu │┌┐└┘─
# ┌────────┐
# │ Name   │
# ├────────┤
# │ Prompt │
# │ Entry 1│
# └────────┘
def styl_menu_vert(name='ExampleMenu',prompt='Please select one of the following:' , entrys=['Entry 1','Entry 2','Entry 3'],description=['The Entry 1 of the menu. Press ENTER to select it','Lorem Ipsulm','LOL'],backcolor='\033[44m',menucolor='\033[47m',selcolor='\033[100m'):
    namel = len(name)
    namelengh = 44-namel
    promptl = 43-len(prompt)
    done = False
    sel = 0
    #Colors
    tres = '\033[39m'
    tblack = '\033[30m'

    while done == False:
        if sel > len(entrys)-1:
            sel = len(entrys)-1
        if sel < 0:
            sel = 0
        print(backcolor+' '*50+'\033[49m')
        print(backcolor+' '*2+menucolor+'┌'+'─'*44+'┐'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+tblack+name+'\033[39m'+' '*namelengh+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'├'+'─'*44+'┤'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+tblack+' '+prompt+'\033[39m'+' '*promptl+'│'+backcolor+' '*2+'\033[49m')
        c = 0
        for object in entrys:
            entry = entrys[c]
            entryl = 42-len(entry)
            if sel == c:
                print(backcolor+' '*2+menucolor+'│'+'  '+selcolor+tblack+entry+tres+menucolor+' '*entryl+'│'+backcolor+' '*2+'\033[49m')
            else:
                print(backcolor+' '*2+menucolor+'│'+'  '+tblack+entry+tres+' '*entryl+'│'+backcolor+' '*2+'\033[49m')
            c += 1
        print(backcolor+' '*2+menucolor+'│'+tblack+' Description:'+tres+' '*31+'│'+backcolor+' '*2+'\033[49m')
        len_desc1 = 42-len(description[sel][0:39])
        len_desc2 = 42-len(description[sel][40:79])
        len_desc3 = 42-len(description[sel][80:120])
        print(backcolor+' '*2+menucolor+'│'+'  '+tblack+description[sel][0:39]+tres+' '*len_desc1+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+'  '+tblack+description[sel][40:79]+tres+' '*len_desc2+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+'  '+tblack+description[sel][80:120]+tres+' '*len_desc3+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'└'+'─'*44+'┘'+backcolor+' '*2+'\033[49m')
        print(backcolor+'\033[34m'+'.'*50+'\033[49m'+'\033[39m')
        keyboard.read_key()
        if keyboard.is_pressed('down'):
            sel += 1
        if keyboard.is_pressed('up'):
            sel -= 1
        if keyboard.is_pressed('enter'):
            done = True
            return sel
        os.system('cls')
    

#print(styl_menu_vert())

def styl_menu_vert_mult(name='ExampleMenu',prompt='Please select one of the following:' , entrys=['Entry 1','Entry 2','Entry 3'],description=['The Entry 1 of the menu. Press ENTER to select it','Lorem Ipsulm','LOL'],backcolor='\033[44m',menucolor='\033[47m',selcolor='\033[100m'):
    selected = []
    for object in entrys:
        selected.append(False)
    namel = len(name)
    namelengh = 44-namel
    promptl = 43-len(prompt)
    done = False
    sel = 0
    #Colors
    tres = '\033[39m'
    tblack = '\033[30m'
    selv = 0

    while done == False:
        if sel > len(entrys)-1:
            sel = len(entrys)-1
        if sel < 0:
            sel = 0
        if selv > 1:
            selv = 1
        if selv < 0:
            selv = 0
        print(backcolor+' '*50+'\033[49m')
        print(backcolor+' '*2+menucolor+'┌'+'─'*44+'┐'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+tblack+name+'\033[39m'+' '*namelengh+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'├'+'─'*44+'┤'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+tblack+' '+prompt+'\033[39m'+' '*promptl+'│'+backcolor+' '*2+'\033[49m')
        c = 0
        for object in entrys:
            entry = ' '+entrys[c]
            if selected[c] == True:
                entry = '*'+entrys[c]+'*'
            entryl = 42-len(entry)
            if sel == c and selv == 0:
                print(backcolor+' '*2+menucolor+'│'+'  '+selcolor+tblack+entry+tres+menucolor+' '*entryl+'│'+backcolor+' '*2+'\033[49m')
            else:
                print(backcolor+' '*2+menucolor+'│'+'  '+tblack+entry+tres+' '*entryl+'│'+backcolor+' '*2+'\033[49m')
            c += 1
        print(backcolor+' '*2+menucolor+'│'+tblack+' Description:'+tres+' '*31+'│'+backcolor+' '*2+'\033[49m')
        len_desc1 = 43-len(description[sel][0:40])
        len_desc2 = 43-len(description[sel][40:80])
        len_desc3 = 43-len(description[sel][80:120])
        print(backcolor+' '*2+menucolor+'│'+' '+tblack+description[sel][0:40]+tres+' '*len_desc1+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+' '+tblack+description[sel][40:80]+tres+' '*len_desc2+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'│'+' '+tblack+description[sel][80:120]+tres+' '*len_desc3+'│'+backcolor+' '*2+'\033[49m')
        if selv==1:
            print(backcolor+' '*2+menucolor+'│'+' '*41+selcolor+tblack+'OK'+menucolor+' '+tres+'│'+backcolor+' '*2+'\033[49m')
        else:
            print(backcolor+' '*2+menucolor+'│'+' '*41+tblack+'OK '+tres+'│'+backcolor+' '*2+'\033[49m')
        print(backcolor+' '*2+menucolor+'└'+'─'*44+'┘'+backcolor+' '*2+'\033[49m')
        print(backcolor+'\033[34m'+'.'*50+'\033[49m'+'\033[39m')
        # Only continue when a key is pressed
        keyboard.read_key()
        if keyboard.is_pressed('down'):
            if selv == 0:
                sel += 1
        if keyboard.is_pressed('up'):
            if selv == 0:
                sel -= 1
        if keyboard.is_pressed('left'):
            selv -= 1
        if keyboard.is_pressed('right'):
            selv += 1
        if keyboard.is_pressed('enter'):
            if selv == 1:
                done = True
                return selected
            else:
                if selected[sel]:
                    selected[sel] = False
                else:
                    selected[sel] = True
        os.system('cls')

#print(styl_menu_vert_mult(entrys=['lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol'],description=['lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol','lol']))
#basic_menu()
import random
import time
import getpass
import sys
def i_play():
    grt = 'größer mehr g m'
    lss = 'kleiner weniger k w'
    rct = 'richtich ja r'
    r = False
    n = False
    sn = "50"
    print('Ich sage es ist '+sn+'.')
    print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
    inp = input().lower()
    if inp in grt:
        sn = str(int(sn) + 25)
        print('Da deine Zahl größer ist, sage ich '+sn+'.')
    elif inp in lss:
        sn = str(int(sn) - 25)
        print('Da deine Zahl kleiner ist, sage ich '+sn+'.')
    else:
        print('Hura! Ich habe deine Zahl erraten.')
        input()
        exit()
    print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
    inp = input().lower()
    inp2 = inp
    if inp in grt:
        while inp2 in grt:
            sn = str(int(sn) + 5)
            print('Ok, wie wäre es mit '+sn+'?')
            print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
            inp2 = input().lower()
            if inp2 in rct:
                print('Hura! Ich habe deine Zahl erraten.')
                input()
                exit()
    elif inp in lss:
        while inp2 in lss:
            sn = str(int(sn) - 5)
            print('Ok, wie wäre es mit '+sn+'?')
            print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
            inp2 = input().lower()
            if inp2 in rct:
                print('Hura! Ich habe deine Zahl erraten.')
                input()
                exit()
    else:
        print('Hura! Ich habe deine Zahl erraten.')
        input()
        exit()
    inp3 = inp
    if inp2 in grt:
        while inp3 in grt:
            sn = str(int(sn) + 1)
            print('Ok, wie wäre es mit '+sn+'?')
            print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
            inp3 = input().lower()
            if inp3 in rct:
                print('Hura! Ich habe deine Zahl erraten.')
                input()
                exit()
    elif inp in lss:
        while inp3 in lss:
            sn = str(int(sn) - 1)
            print('Ok, wie wäre es mit '+sn+'?')
            print('Ist deine Zahl "Größer" oder "Kleiner" oder "Richtich"?')
            inp3 = input().lower()
            if inp3 in rct:
                print('Hura! Ich habe deine Zahl erraten.')
                input()
                exit()
    else:
        print('Hura! Ich habe deine Zahl erraten.')
        input()
        exit()
ans = True
pw = getpass.getpass(prompt='Password: ', stream=None)
if pw.lower() == 'juni':
    x = True
elif pw.lower() == 'ihavetheforce':
    i_play()
elif pw.lower() == 'iplaynow':
    i_play()
elif pw.lower() == 'iplay':
    i_play()
elif pw.lower() == 'i':
    i_play()
else:
    x = False
while ans != False:
    num = random.randrange(10,99)
    print('Wilkommen zum Zahlenraten.')
    print('Errate meine zweistellige Zahl.')
    if x:
        print('Tipp: Die zahl liegt im bereich der '+str(num)[:1]+'0')
    n = False
    while n != True:
        inp = int(input('Dein versuch: '))
        if inp > num:
            print('Meine Zahl ist Kleiner.')
        if inp < num:
            print('Meine Zahl ist Größer.')
        if inp == num:
            print('Du hast meine Zahl erraten!.')
            print('Nochmal? (J/N)')
            p = input()
            if p.lower() == 'n':
                ans = False
            n = True
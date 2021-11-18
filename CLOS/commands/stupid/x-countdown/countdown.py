import color as style
import datetime
import keyboard
import platform
import time
import json
import os

# Functions

# Clear terminal
if 'Windows' in platform.system():
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

# time converter htl (high[er value] to low[er value])
def timeconhtl(timea, timebpera = 60, retunr='both'):
    # Get number of "houres" out of time a
    hour = int(timea/timebpera)
    # Removes "Houres" from original time
    timearem = timea-hour*timebpera
    # Returns "Houres" and left time
    if retunr == 'both':
        return timearem, hour
    elif retunr == 'houre':
        return hour
    elif retunr == 'minutes':
        return timearem

# Load settings:
setf = open(os.path.dirname(os.path.realpath(__file__)) + '\config.json', 'r')
setting = json.loads(setf.read())
setf.close()
clock = setting["clock"]
name = ' '+setting["name"] + setting["space_after_name"]
finished = False
done = False

while not keyboard.is_pressed('q') and not done:
    # color
    print(style.color.Red+style.backcolor.BackgroundDefault)
    # calculate time between now and target
    curtime = datetime.datetime.now()
    tartime = datetime.datetime(setting["year"], setting["month"], setting["day"], setting["houre"], setting["minute"], setting["second"])
    remtime = tartime-curtime
    # check for more then 0 days in counter
    if 'day' in str(remtime):
        splitday = str(remtime).split(' ')
        splittime = splitday[2].split(':')
        #print(remtime,splittime,splitday[2])
        #print(str(splitday[0]), str(splitday[1]) + ' ' + str(splittime[0])+ ' h',)
        splitms = splittime[2].split('.')
        if int(splitday[0]) > 365:
            day, year = timeconhtl(int(splitday[0]), 365)
        else:
            day = splitday[0]
            year = 0

        if year > 0:
            years = str(year) + ' Year(s) '
        else:
            years = ''

        if int(day) > 0:
            days = str(day) + ' Day(s) '
        else:
            days = ''
    else:
        splittime = str(remtime).split(':')
        splitms = splittime[2].split('.')
        days = ''
        years = ''
    # Remaining Time
    if int(splittime[0]) == 0:
        if int(splittime[1]) == 0:
            if int(splitms[0]) == 0:
                finished = True
                c = 0
    if finished:
        c = c + 1
        dtime = '  0h 0m 0s 0ms '
        if c == 2:
            time.sleep(5)
            done = True
    else:
        dtime = '  '+years + days + str(splittime[0]) + 'h ' + str(splittime[1]) + 'm ' + str(splitms[0]) + 's ' + str(splitms[1])[:2] + 'ms '
    # if needed, extra spaces
    if len(name) < len(dtime):
            extra=len(dtime)-len(name)
            extra2 = 0
    else:
        extra = 0
        extra2 = len(name)-len(dtime)
    space = len(name)+extra
    #time.sleep(0.5)
    # check if clock is enables -> disaplay clock +style.format.Bold
    if clock:
        time.sleep(.5)
        clear()
        print("                   ║" + datetime.datetime.now().strftime("%d:%m:%Y") + "  " + datetime.datetime.now().strftime("%H:%M:%S") + "║")
        print("                   ╚════════════════════╝")
    else:
        time.sleep(.5)
        clear()
        print("")
        print("")
    # display countdown
    print("")
    print("")
    print("")
    print("")
    print("                   ╔"+space*"═"+"╗")
    print("                   ║"+style.format.Underlined+name +extra*' '+style.format.ResetUnderlined+"║")
    print("                   ║" + dtime + extra2*' ' + "║")
    print("                   ╚"+space*"═"+"╝")

print(style.color.Default+style.backcolor.BackgroundDefault)

# Countdown Finished executions \/
import win10toast
import threading
import datetime
import platform
import pathlib
import sys
import os

relpath = os.path.dirname(os.path.realpath(__file__))
auto = 'C:\\Users\\'+os.getlogin+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\reminder_autostart.bat'
Path = pathlib.Path
arg = sys.argv

def checker

if len(arg) > 1:
    #if not Path(auto).is_file():
        #if 'Windows' in platform.system():
        #f = open(auto)
            #f.write('')
    if 'start' in arg:

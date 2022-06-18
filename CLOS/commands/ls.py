from cmath import exp
from concurrent.futures.process import EXTRA_QUEUED_CALLS
import os

def text_rgb(r=0, g=255, b=50):
    return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'
def back_rgb(r=0, g=255, b=50):
    return '\033[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

class underline:
    UNDERLINED = '\033[4m'
    RESET_UNDERLINED = '\033[24m'

class color:
    Default      = '\033[39m'
    Black        = '\033[30m'
    White        = '\033[97m'
    Red          = '\033[31m'
    Green        = '\033[32m'
    Yellow       = '\033[33m'
    Blue         = '\033[34m'
    Magenta      = '\033[35m'
    Cyan         = '\033[36m'
    LightGray    = '\033[37m'
    LightRed     = '\033[91m'
    LightGreen   = '\033[92m'
    LightYellow  = '\033[93m'
    LightBlue    = '\033[94m'
    LightMagenta = '\033[95m'
    LightCyan    = '\033[96m'
    DarkGray     = '\033[90m'

res = '\033[39m'+'\033[24m'

def getObjectinFolder(dir = os.path.dirname(os.path.realpath(__file__)), blacklist = [""], onlyfiles = True):
    x = []
    objects = os.listdir(dir)
    file_objects = [f for f in objects if os.path.isfile(os.path.join(dir, f))]
    if onlyfiles:
        objlist = file_objects
    else:
        objlist = objects
    for object in objlist:
        if not object in blacklist:
            x.append(object)
    return x

content = getObjectinFolder(os.getcwd(), onlyfiles=False)

content_folders = []
content_files =   []

for o in content:
    if os.path.isfile(o):
        try:
            x = 13-len(o.split('.')[1].upper().replace('PY', 'Python').replace('TXT', 'Text')+' File ')
            content_files.append(o.split('.')[1].upper().replace('PY', color.Yellow+'Python').replace('TXT', 'Text').replace('JSON', color.Cyan+'Json')+' File '+res+' '*x+'| '+o)
        except:
            content_files.append('File         | '+o)
    else:
        content_folders.append(color.LightBlue+'Folder       '+res+'| '+o)

# Display Contents:
print(underline.UNDERLINED+' Type:        | Name:                '+res)
for o in content_folders:
    print(' '+o)
for o in content_files:
    print(' '+o)
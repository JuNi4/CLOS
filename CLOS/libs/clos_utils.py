import os
import sys
import json
import platform
from pathlib import Path

class commands():
    def __init__(self):
        self.fpath = os.environ["CLOS_DIR"]

    def command(command = 'none'):
        if 'Windows' in platform.system():
            pjf = open(os.path.dirname(os.path.realpath(__file__))+'\\dirs.json', 'r')
        else:
            pjf = open(os.path.dirname(os.path.realpath(__file__)) + '/dirs.json', 'r')
        pj = json.loads(pjf.read())
        pjf.close()
        dirs = pj["CLOS_DIR"]
        if ' ' in command:
            command1 = str(command).split()
            commandf = command1[0]
            x = command[len(commandf):]
        else:
            commandf = command
            x = ''
        # Check in command dir
        fc = dirs + '/commands/' + commandf + '.py'
        # Check in current dir
        fp = os.getcwd() + '/' + commandf
        #print(fc)
        #print(fp)
        command_file = Path(fc)
        if command_file.is_file():
            os.system(str(fc) + x)
        else:
            current_file = Path(fp)
            if current_file.is_file():
                if 'Windows' in platform.system():
                    os.system('python '+commandf + x)
                else:
                    os.system('python3 '+commandf + x)
            else:
                print('No File or Command found caled ' + commandf+ '. Use the \'help\' command for a list of all available commands.')

class utils():
    def __init__(self, prog_arrow_tip = '>', prog_arrow_body = '-'):
        self.prarrow_t = prog_arrow_tip
        self.prarrow_b = prog_arrow_body

    def progressBar(self,current, total = 100, barLength = 20):
        percent = float(current) * 100 / total
        arrow   = self.prarrow_b * int(percent/100 * barLength - 1) + self.prarrow_t
        spaces  = ' ' * (barLength - len(arrow))

        bar = '[%s%s] %d %%' % (arrow, spaces, percent)

        return bar

    def ifcolor(text = 'Example Text', color = '\033[32m', defaultcolor = '\033[39m'+'\033[49m'):
        if 'Windows' in platform.system():
            pjf = open(os.path.dirname(os.path.realpath(__file__))+'\dirs.json', 'r')
        else:
            pjf = open(os.path.dirname(os.path.realpath(__file__)) + '/dirs.json', 'r')
        pj = json.loads(pjf.read())
        pjf.close()
        data = pj["DATA_DIR"]

        if 'Windows' in platform.system():
            boot_optf = open(data+'\\boot_opt.json', 'r')
        else:
            boot_optf = open(data+'/boot_opt.json', 'r')
        boot_opt = json.loads(boot_optf.read())
        boot_optf.close()
        color_enable = boot_opt["color_enabled"]

        if color_enable:
            return color + text + defaultcolor
        else:
            return text

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

    def if_win():
        if 'Windows' in platform.system():
            return True
        else:
            return False

    def getarg(arg, alt):
        if not arg == '':
            if arg in sys.argv:
                return sys.argv[sys.argv.index(arg) + 1]
            else:
                return alt

class text_style():
    res = '\033[21m'+'\033[22m'+'\033[24m'+'\033[25m'+'\033[27m'+'\033[28m'+'\033[39m'+'\033[49m'
    def text_rgb(r=0, g=255, b=50):
        return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'
    def back_rgb(r=0, g=255, b=50):
        return '\033[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'
    class format:
        ResetBold       = '\033[21m'
        ResetDim        = '\033[22m'
        ResetUnderlined = '\033[24m'
        ResetBlink      = '\033[25m'
        ResetReverse    = '\033[27m'
        ResetHidden     = '\033[28m'

        Bold       = '\033[1m'
        Dim        = '\033[2m'
        Underlined = '\033[4m'
        Blink      = '\033[5m'
        Reverse    = '\033[7m'
        Hidden     = '\033[8m'

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

    class backcolor:
        Default      = '\033[49m'
        Black        = '\033[40m'
        Red          = '\033[41m'
        Green        = '\033[42m'
        Yellow       = '\033[43m'
        Blue         = '\033[44m'
        Magenta      = '\033[45m'
        Cyan         = '\033[46m'
        LightGray    = '\033[47m'
        DarkGray     = '\033[100m'
        LightRed     = '\033[101m'
        LightGreen   = '\033[102m'
        LightYellow  = '\033[103m'
        LightBlue    = '\033[104m'
        LightMagenta = '\033[105m'
        LightCyan    = '\033[106m'
        White        = '\033[107m'

if __name__ == '__main__':
    print('ugh.. this is a libary for CLOS and nothing to see here...')
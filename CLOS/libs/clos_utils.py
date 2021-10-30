import os
import json
from pathlib import Path

class commands():
    def __init__(self):
        self.fpath = os.environ["CLOS_DIR"]

    def command(command = 'none'):
        pjf = open(os.path.dirname(os.path.realpath(__file__))+'\dirs.json', 'r')
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
        fc = dirs + '\commands\\' + commandf + '.py'
        # Check in current dir
        fp = os.getcwd() + '\\' + commandf
        print(fc)
        print(fp)
        command_file = Path(fc)
        if command_file.is_file():
            os.system(str(fc) + x)
        else:
            current_file = Path(fp)
            if current_file.is_file():
                os.system(commandf + x)
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

class text_style():
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
# echo %time:~0,2% Houres and %time:~3,2% minutes and %time:~6,2% seconds
# Color command from Windows CMD:
import sys
arg = sys.argv
helptxt_de = 'Legt die standardmäßigen Hinter- und Vordergrundfarben für die Konsole fest.\n\nCOLOR [attr]\n\n  attr      Gibt die Farbattribute für die Konsolenausgabe an.\n\nFarbattribute werden durch ZWEI hexadezimale Zeichen angegeben – das erste\nbezieht sich auf den Hintergrund, das zweite auf den Vordergrund. Jedes Zeichen\nkann einen der folgenden Werte annehmen:\n\n    0 = Schwarz   8 = Grau\n    1 = Blau      9 = Hellblau\n    2 = Grün      A = Hellgrün\n    3 = Türkis    B = Helltürkis\n    4 = Rot       C = Hellrot\n    5 = Lila      D = Helllila\n    6 = Gelb      E = Hellgelb\n    7 = Hellgrau  F = Weiß\n                  R = Reset\n\nWenn der Befehl ohne Argument aufgerufen wird, werden die Farbein-\nstellungen wiederhergestellt, mit denen CMD.EXE gestartet wurde. Diese werden\ndurch das aktuelle Konsolenfenster, die /T-Befehlszeilenoption oder durch den\nRegistrierungswert "DefaultColor" bestimmt.\n\nDer COLOR-Befehl legt ERRORLEVEL auf 1 fest, wenn versucht wird,\ndiesen Befehl mit einer Vordergrundfarbe auszuführen, die mit der Hinter-\ngrundfarbe identisch ist.\n\nBeispiel: "COLOR fc" generiert Hellrot auf weißem Hintergrund.'
helptxt_en = 'Sets the default console foreground and background colors.\n\nCOLOR [attr]\n\n  attr        Specifies color attribute of console output\n\nColor attributes are specified by TWO hex digits -- the first\ncorresponds to the background; the second the foreground.  Each digit\ncan be any of the following values:\n\n    0 = Black       8 = Gray\n    1 = Blue        9 = Light Blue\n    2 = Green       A = Light Green\n    3 = Aqua        B = Light Aqua\n    4 = Red         C = Light Red\n    5 = Purple      D = Light Purple\n    6 = Yellow      E = Light Yellow\n    7 = White       F = Bright White\n                    R = Reset\n\nIf no argument is given, this command restores the color to what it was\nwhen CMD.EXE started.  This value either comes from the current console\nwindow, the /T command line switch or from the DefaultColor registry\nvalue.\n\nThe COLOR command sets ERRORLEVEL to 1 if an attempt is made to execute\nthe COLOR command with a foreground and background color that are the\nsame.\n\nExample: "COLOR fc" produces light red on bright white'

res = '\033[21m'+'\033[22m'+'\033[24m'+'\033[25m'+'\033[27m'+'\033[28m'+'\033[39m'+'\033[49m'
def text_rgb(r=0, g=255, b=50):
    return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'
def back_rgb(r=0, g=255, b=50):
    return '\033[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

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

class bcolor:
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

colors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','R']
corospondst = [color.Black,color.Blue,color.Green,color.Cyan,color.Red,color.Magenta,color.Yellow,color.LightGray,color.DarkGray,color.LightBlue,color.LightGreen,color.LightCyan,color.LightRed,color.LightMagenta,color.LightYellow,color.White,color.Default]
corospondsb = [bcolor.Black,bcolor.Blue,bcolor.Green,bcolor.Cyan,bcolor.Red,bcolor.Magenta,bcolor.Yellow,bcolor.LightGray,bcolor.DarkGray,bcolor.LightBlue,bcolor.LightGreen,bcolor.LightCyan,bcolor.LightRed,bcolor.LightMagenta,bcolor.LightYellow,bcolor.White,bcolor.Default]
if len(arg) == 1 or sys.argv[1] == '/?':
    print(helptxt_en)
    exit()
else:
    if arg[1] == '-frgb':
        if len(arg) >= 5:
            print(text_rgb(arg[2],arg[3],arg[4]))
        elif len(arg) >= 4:
            print(text_rgb(arg[2],arg[3],0))
        elif len(arg) >= 3:
            print(text_rgb(arg[2],0,0))
        else:
            print('-frgb requieres at least 1 rgb value (0-255)')
    elif arg[1] == '-brgb':
        if len(arg) >= 5:
            print(back_rgb(arg[2],arg[3],arg[4]))
        elif len(arg) >= 4:
            print(back_rgb(arg[2],arg[3],0))
        elif len(arg) >= 3:
            print(back_rgb(arg[2],0,0))
        else:
            print('-brgb requieres at least 1 rgb value (0-255)')
    elif arg[1] == 'reset':
        print(color.Default+bcolor.Default, end = "")
        exit()
    elif len(arg[1]) == 2 and arg[1][1:2].upper() in colors and arg[1][:1].upper() in colors:
        print(corospondst[colors.index(arg[1][1:2].upper())], end = "")
        print(corospondsb[colors.index(arg[1][:1].upper())], end = "")
    elif arg[1][:1].upper() in colors:
        print(corospondst[colors.index(arg[1][:1].upper())], end = "")
    else:
        x = ''
        x2 = ''
        if not arg[1][1:2].upper() in colors:
            x = arg[1][1:2].upper()
        if not arg[1][:1].upper() in colors:
            x2 = arg[1][:1].upper()
        if not x2 == '':
            x = x2 + ', ' + x
        print('Invalid [attr]: '+x)
import clos_command, sys, os, json

clos_command.command_name = "theme"

# Import other libs
clos_command.libPath()
import clos_utils

DIRS = clos_command.CLOSDirs()

if "error" in DIRS:
    print("An error accoured in clos_command while getting the directorys: "+DIRS["error"])
    exit(1)

THEME_DIR = DIRS["CLOS_DIR"]+"/themes"

LANG = clos_command.getLanguageFile()

def listAllThemes():
    themes = {}
    # Go throug all objects in themes
    for o in os.listdir(THEME_DIR):
        # Only return json files
        if ".json" in o:
            # Open file to see if it has the theme id key
            with open(THEME_DIR+"/"+o) as f:
                x = json.loads(f.read())
                if "themeID" in x:
                    themes[o.replace(".json","")] = {"id": x["themeID"], "name": x["themeName"]}

    return themes

colors = {
    "default": "clos_utils.text_style.color.Default",
    "black": "clos_utils.text_style.color.Black",
    "white": "clos_utils.text_style.color.White",
    "red": "clos_utils.text_style.color.Red",
    "green": "clos_utils.text_style.color.Green",
    "yellow": "clos_utils.text_style.color.Yellow",
    "blue": "clos_utils.text_style.color.Blue",
    "magenta": "clos_utils.text_style.color.Magenta",
    "cyan": "clos_utils.text_style.color.Cyan",
    "light_gray": "clos_utils.text_style.color.LightGray",
    "light_red": "clos_utils.text_style.color.LightRed",
    "light_green": "clos_utils.text_style.color.LightGreen",
    "light_yellow": "clos_utils.text_style.color.LightYellow",
    "light_blue": "clos_utils.text_style.color.LightBlue",
    "lightMagenta": "clos_utils.text_style.color.LightMagenta",
    "light_cyan": "clos_utils.text_style.color.LightCyan",
    "dark_gray": "clos_utils.text_style.color.DarkGray"
}

backgrounds = {
    "default": "clos_utils.text_style.background.Default",
    "black": "clos_utils.text_style.background.Black",
    "white": "clos_utils.text_style.background.White",
    "red": "clos_utils.text_style.background.Red",
    "green": "clos_utils.text_style.background.Green",
    "yellow": "clos_utils.text_style.background.Yellow",
    "blue": "clos_utils.text_style.background.Blue",
    "magenta": "clos_utils.text_style.background.Magenta",
    "cyan": "clos_utils.text_style.background.Cyan",
    "light_gray": "clos_utils.text_style.background.LightGray",
    "light_red": "clos_utils.text_style.background.LightRed",
    "light_green": "clos_utils.text_style.background.LightGreen",
    "light_yellow": "clos_utils.text_style.background.LightYellow",
    "light_blue": "clos_utils.text_style.background.LightBlue",
    "lightMagenta": "clos_utils.text_style.background.LightMagenta",
    "light_cyan": "clos_utils.text_style.background.LightCyan",
    "dark_gray": "clos_utils.text_style.background.DarkGray"
}

def getTxtColor(cOBJ):
    # Check color name
    if type(cOBJ) == str:
        if cOBJ in colors:
            return eval(colors[cOBJ])
    # RGB Values
    if type(cOBJ) == dict:
        if "r" in cOBJ and "g" in cOBJ and "b" in cOBJ:
            return clos_utils.text_style.text_rgb(cOBJ["r"],cOBJ["g"],cOBJ["b"])

def getBgrColor(cOBJ):
    # Check color name
    if type(cOBJ) == str:
        if cOBJ in backgrounds:
            return eval(backgrounds[cOBJ])
    # RGB Values
    if type(cOBJ) == dict:
        if "r" in cOBJ and "g" in cOBJ and "b" in cOBJ:
            return clos_utils.text_style.back_rgb(cOBJ["r"],cOBJ["g"],cOBJ["b"])

#########################
## Theme maneger stuff ##
#########################
print(__file__)
if __name__ in "__main__":

    themes = listAllThemes()

    ids = []

    # get a list of all theme ids
    for o in themes:
        ids.append(themes[o]["id"])

    # try to get the requested theme
    try:
        x = sys.argv[1]
    except:
        x = ""

    # applie a requested theme
    if len(sys.argv) >= 1 and (x in themes or x in ids):
        print("Applying "+o,end="")
        # Load theme file
        if x in themes:
            file = open(DIRS["CLOS_DIR"]+"/themes/"+x+".json")
        else:
            file = open(DIRS["CLOS_DIR"]+"/themes/"+themes[ids.index(x)]+".json")

        # read file
        theme = json.loads(file.read())
        file.close()

        # Text color
        if "text_color" in theme:
            print(getTxtColor(theme["text_color"]), end="")

        print()

    # Load saved theme
    elif len(sys.argv) >= 1 and x == "load":
        pass
        
    # Help message if no arguments are applied
    else:
        print('You need to select a theme. The following themes are available:')
        # print all themes
        for o in themes:
            print(" - "+o+": "+themes[o]["name"])

        print("\nYou can aply any theme by typing 'theme [id or name]'.")
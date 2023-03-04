import json,os,sys

PATH = os.path.abspath(os.path.dirname(__file__))

command_name = "donut"

def CLOSDirs():
    # check if dirs file exists
    if not os.path.isfile(PATH+"/dirs.json"):
        return {"error": "dirs file does not exist"}
    
    # Read file
    f = open(PATH+"/dirs.json")
    x = json.loads(f.read())
    f.close()

    return x

def libPath():
    sys.path.append(CLOSDirs()["LIB_DIR"])

def getLanguageFile():
    # Get the language file
    ## Read settings file
    SDIR = CLOSDirs()["DATA_DIR"]
    setting_file = open(SDIR+"/settings.json")
    setting = json.loads(setting_file.read())
    setting_file.close()

    # Language id
    lang = setting["lan"]

    # Load language file
    lang_file = CLOSDirs()["COMMAND_DATA_DIR"]+"/"+command_name+"/language_"+lang+".json"
    if not os.path.isfile(lang_file):
        return {"error:" "command language file does not exist"}
    
    # Read from file
    l_file = open(lang_file)
    lang = json.loads(l_file.read())
    l_file.close()

    return lang
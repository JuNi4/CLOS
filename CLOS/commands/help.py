# Help command
import os
import sys
import json

# Get the path of the current file
path = os.path.dirname(os.path.realpath(__file__))

# open dirs.json
with open(path + '/dirs.json') as json_file:
    dirs = json.load(json_file)

# Append Libsdir to path
sys.path.append(dirs['LIB_DIR'])
# Import CLOS_utils
from clos_utils import *
import translations

# Get settings file
settings_file = dirs['DATA_DIR'] + '/settings.json'
# Open settings file
with open(settings_file) as json_file:
    settings = json.load(json_file)

translations.lang_name = settings["lan"]

# Get name of every command and filter out every non python file
commands = [f.split('.')[0] for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.py')]

# All internal Clos commands
internal_commands = ['redo_setup','setup','exit','shutdown','reboot','sys','python']

# Print internal commands
print(text_style.format.Underlined+translations.lang('help.internal_commands')+text_style.format.ResetUnderlined)
for i in range(len(internal_commands)):
    print(internal_commands[i] + ': ' +text_style.color.DarkGray+ translations.sub_lang(internal_commands[i],"help.internal_commands.discription")+text_style.res)

# Print commands with their description
print(text_style.format.Underlined+translations.lang('help.available_commands')+text_style.format.ResetUnderlined)
for command in commands:
    # check if cammnd.json is file
    if os.path.isfile(dirs["COMMAND_DATA_DIR"] + '/' + command + '.json'):
        with open(os.path.join(dirs["COMMAND_DATA_DIR"], 3 + '.json')) as f:
            data = json.load(f)
            print(command + ': ' + data['description'])
    else:
        print(command +text_style.color.DarkGray+': No description available'+text_style.res)
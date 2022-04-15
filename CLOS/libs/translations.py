import json
import os
import sys

# Get the path of the current file
path = os.path.dirname(os.path.realpath(__file__))

# Open dirs.json
with open(path + '/dirs.json') as json_file:
    dirs = json.load(json_file)

lang_name = 'en_us'
lang_path = dirs["LANG_DIR"]

# Get value from language file by json key
def lang(json_key = ''):
    # Check if langfile exists
    if not os.path.isfile(lang_path + '/' + lang_name + '.json'):
        return json_key
    # Open language file
    with open(lang_path + '/' + lang_name + '.json') as json_file:
        data = json.load(json_file)
        # Return value
        if json_key in data:
            return data[json_key]
        else:
            return json_key

def sub_lang(json_key = '', parent_value = ''):
    # Check if langfile exists
    if not os.path.isfile(lang_path + '/' + lang_name + '.json'):
        return parent_value+'['+json_key+']'
    # Open language file
    with open(lang_path + '/' + lang_name + '.json') as json_file:
        data = json.load(json_file)
        # Return value
        if parent_value in data:
            if json_key in data[parent_value]:
                return data[parent_value][json_key]
            else: return parent_value+'['+json_key+']'
        else: return parent_value+'['+json_key+']'
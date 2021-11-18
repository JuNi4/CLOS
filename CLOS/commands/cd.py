# -----------
# CLOS V 0.1 Command 'cd'
# Credits: JuNi (https://github.com/JuNi4/CLOS)
# -----------
import platform
import json
import sys
import os

# Just to enable debug messages
debug = 0
if debug:
    print('Debug Info: '+platform.system())

# Do stuff for importing libraries from CLOS Libs folder:
# Opens the 'dirs.json' to get the path for CLOS Libs
if 'Windows' in platform.system():
    f = open(os.path.dirname(os.path.realpath(__file__))+'\\dirs.json', 'r')
else:
    f = open(os.path.dirname(os.path.realpath(__file__))+'/dirs.json', 'r')

# Reads contents from dirs.json
dirs = json.loads(f.read())
f.close()

# Appends CLOS Lib dir to sys.path temporaily
sys.path.append(dirs["LIB_DIR"])

# Debug Info:
if debug:
    print('Debug Info: '+str(dirs))
    print('Debug Info: '+dirs["LIB_DIR"])
    print('Debug Info: Args: '+str(sys.argv))

#import color # the color module is outdated - now everything is in CLOS Util
import clos_utils

# Get Arguments:
arg = sys.argv

# Check if args are present (argv len() > 1)
if len(arg) > 1:
    if arg[1] == '..':
        os.system('cd D:\Justus\Dokumente')
        print('lol')
else:
    print(os.system('echo %cd%'))
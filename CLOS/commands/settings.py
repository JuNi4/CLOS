# Clos JuNi Jumpstart
# Import
import os
import sys
import json
import platform
from pathlib import Path

# Vars
#  Relpath
relpath = os.path.dirname(os.path.realpath(__file__))
#  Spacer (/ or \\)
if 'Windows' in platform.system(): sp = '\\'
else: sp = '/'
# dirs.json
dirs = relpath+sp+'dirs.json'

#  Check for dirs.json if not exists CRASH
if not Path(dirs).is_file():
    print('\033[41m'+'Error: dirs.json not found. This command needs to be used with CLOS'+'\033[49m')
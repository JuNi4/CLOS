Commands Folder. Use Python Files. Is Main Folder For Commands. The name of the file is the command.
So if a file woulld be called test(.py), if you would type test into the terminal, it would execute the test.py file.

If it requires adminestrator perms on linux, put it in sudo/sudo.json under "objects"
If you just want it to require a password, add this code to your command:

# Import librarys. if you already imported those, leave this part out
import json
import platform

# Check if file has pw flag
def check_pw():
    sp = '/'
    if 'Windows' in platform.system():
        sp = '\\'
    sudof = open('sudo'+sp+'pw.json', 'r')
    sudo = json.loads(dirsf.read())
    sudof.close()
    if ''
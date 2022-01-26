from cmath import exp
from concurrent.futures.process import EXTRA_QUEUED_CALLS
import os

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

content = getObjectinFolder(os.getcwd(), onlyfiles=False)

content_folders = []
content_files =   []

for o in content:
    if os.path.isfile(o):
        try:
            x = 11-len(o.split('.')[1].upper()+' File')
            content_files.append(o.split('.')[1].upper()+' File'+' '*x+o)
        except:
            content_files.append('File       '+o)
    else:
        content_folders.append('Folder     '+o)

# Display Contents:
print(' Type:    | Name:')
for o in content_folders:
    print(' '+o)
for o in content_files:
    print(' '+o)
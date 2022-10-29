# Image Viewer like in the Messenger
from argparse import FileType
from multiprocessing import managers
import tkinter as tk
from tkinter import filedialog
import json
import sys
import os

f = open(os.path.dirname(os.path.relpath(__file__))+'/dirs.json')
dirs = json.loads(f.read())
f.close()

# import stuff
sys.path.append(dirs["LIB_DIR"])

from itj2 import itj
from itj2 import tests

# Load files from args
#try:
if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        if sys.argv[1].endswith('.json'):
            f = open(sys.argv[1], 'r')
            sendspl = f.read()
            f.close()
        elif sys.argv[1].endswith('.png') or sys.argv[1].endswith('.jpg'):
            sendspl = itj.img_to_json(1, 1, sys.argv[1])

        ij = json.loads(sendspl)
        w = int(ij["w"])
        h = int(ij["h"])
        w2 = w
        h2 = h
        sc = 1
        print('OLD W&H: '+str(w)+' '+str(h))
        # shrink image down if needed
        while w2 > 76 or h2 > 76:
            sc += 1
            w2 = int(w/sc)
            h2 = int(h/sc)
        # get calculated shrink values and shrink
        print('NEW W&H: '+str(w2)+' '+str(h2)+' AND SCALE: '+str(sc))
        sendspl = itj.manage_json(1, sc, json2= sendspl)
        itj.json_to_text(1, 1,json2 = sendspl)
#except Exception as e:
#    print(e)

root = tk.Tk()
root.withdraw()

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def open_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

# Main Loop
while True:
    # Wait for any key to be released
    x = input(">")

    # If the key is 'q'
    if x == 'q' or x == 'quit' or x == 'exit':
        exit()
    # If the key is 'o'
    elif x == 'o' or x == 'open':
        fp = filedialog.askopenfile(filetypes=[('image files','.png .jpg')])
        try:
            if not fp.name: continue
            fp = str(fp.name)
        except:
            continue
        # check if the file is an image
        if fp.endswith('.jpg') or fp.endswith('.png') or fp.endswith('.gif'):
            # Open Image
            sendspl = itj.img_to_json(1,1,fp)
            # Load text to json
            ij = json.loads(sendspl)
            w = int(ij["w"])
            h = int(ij["h"])
            w2 = w
            h2 = h
            sc = 1
            print('OLD W&H: '+str(w)+' '+str(h))
            # shrink image down if needed
            while w2 > 38*2 or h2 > 38*2:
                sc += 1
                w2 = int(w/sc)
                h2 = int(h/sc)
            # get calculated shrink values and shrink
            print('NEW W&H: '+str(w2)+' '+str(h2)+' AND SCALE: '+str(sc))
            sendspl = itj.manage_json(1,sc,sendspl)
            # Display Image
            itj.json_to_text(json2 = sendspl)
    # If the key is 's'
    elif x == 's' or x == 'save':
        if sendspl:
            #fp = open_folder()
            fp = filedialog.asksaveasfilename(filetypes=[('image files','.png .jpg')])
            if not fp: continue
            # Save Image
            itj.json_to_image(json2 = sendspl, output = fp)
    elif x == 'genTestImg':
        sendspl = tests.generateRandomImage()
        itj.json_to_text(json2 = sendspl)
    elif x == 'export':
        fp = filedialog.asksaveasfilename(filetypes=[('json files','.json')])
        if not fp: continue
        # Export Json
        f = open(fp, 'w')
        f.write(sendspl)
        f.close()
    elif x == 'import':
        # Open A file to import
        fp = filedialog.askopenfile(filetypes=[('json files', '.json')])
        f = open(fp.name, 'r')
        # Read content
        sendspl = f.read()
        f.close()
        # Dispaly the image
        itj.json_to_text(json2=sendspl)
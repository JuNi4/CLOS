# Image Viewer like in the Messenger
import tkinter as tk
from tkinter import filedialog
import keyboard
import json
import sys
import os

f = open(os.path.dirname(os.path.relpath(__file__))+'/dirs.json')
dirs = json.loads(f.read())
f.close()

# import stuff
sys.path.append(dirs["LIB_DIR"])

from itj2 import itj


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
    x = keyboard.normalize_name(keyboard.read_key())

    # If the key is 'q'
    if x == 'q':
        exit()
    # If the key is 'o'
    elif x == 'o':
        fp = open_file()
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
    elif x == 's':
        if sendspl:
            fp = open_folder()
            # Save Image
            itj.json_to_image(json2 = sendspl, output = fp+'/img.png')
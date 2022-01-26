# Pillow to read every pixel from a image
from email.mime import image
import platform
from PIL import Image
# Json for img to json convertion and vice versa
import json
import sys

# Empfolenes Maximum: 38x38

class itj():
        
    class color():
        r = '\033[1;0m'
        def rgb(r=0,g=255,b=50):
            return '\033[38;2;'+str(r)+';'+str(g)+';'+str(b)+'m'

    def img_to_text(scling = 1, shrink = 1, img = 'img.png', rgb = color.rgb, r = color.r):
        scling = int(scling)
        shrink = int(shrink)
        img = Image.open(img)
        img = img.convert('RGB')
        scaling = img.size
        i = 0
        while i+shrink <= scaling[1]:
            i2 = 0
            pval = ''
            while i2+shrink <= scaling[0]:
                val = img.getpixel((i2,i))
                pval = pval+rgb(val[0], val[1], val[2])+'██'*scling
                i2 += shrink
            i += shrink
            print(pval+r)

    def img_to_json(scling = 1, shrink = 1, img = 'img.png', rgb = color.rgb, r = color.r):
        jo = {
            "name": "lol",
            "w": 0,
            "h": 0,
            "pix": []
        }
        jol = json.loads(json.dumps(jo))
        sp = '/'
        if 'Windows' in platform.system():
            sp = '\\'
        jol["name"] = img.split(sp)[len(img.split(sp))-1]
        scling = int(scling)
        shrink = int(shrink)
        img = Image.open(img)
        img = img.convert('RGB')
        scaling = img.size
        jol["w"] = int(scaling[0]/shrink)
        jol["h"] = int(scaling[1]/shrink)
        i = 0
        while i+shrink <= scaling[1]:
            i2 = 0
            pval = []
            while i2+shrink <= scaling[0]:
                val = img.getpixel((i2,i))
                pval.append([val[0],val[1],val[2]])
                i2 += shrink
            i += shrink
            jol["pix"].append(pval)
        return json.dumps(jol, indent=4)
    
    def json_to_text(scling = 1, shrink = 1, json2 = '{"name": "lol", "w": 0, "h": 0, "pix":[[],[]]}', rgb = color.rgb, r = color.r):
        img = json.loads(json2)
        scling = int(scling)
        shrink = int(shrink)
        scaling = (img["w"]*scling,img["h"]*scling)
        i = 0
        while i+shrink <= scaling[1]:
            i2 = 0
            pval = ''
            while i2+shrink <= scaling[0]:
                val = img["pix"][i][i2]
                pval = pval+rgb(val[0], val[1], val[2])+'██'*scling
                i2 += shrink
            i += shrink
            print(pval+r)

    def manage_json(scling = 1, shrink = 1, json2 = '{"name": "lol", "w": 0, "h": 0, "pix":[[0,0,0],[]]}', rgb = color.rgb, r = color.r):
        jo = {
            "name": "lol",
            "w": 0,
            "h": 0,
            "pix": []
        }
        jol = json.loads(json.dumps(jo))
        img = json.loads(json2)
        scling = int(scling)
        shrink = int(shrink)
        jol["name"] = img["name"]
        jol["w"] = int(img["w"]/shrink)*scling
        jol["h"] = int(img["h"]/shrink)*scling
        scaling = (img["w"],img["h"])
        i = 0
        while i+shrink <= scaling[1]:
            i2 = 0
            pval = []
            while i2+shrink <= scaling[0]:
                val = img["pix"][i][i2]
                for i3 in range(0,scling):
                    pval.append([val[0],val[1],val[2]])
                i2 += shrink
            i += shrink
            for i3 in range(0,scling):
                jol["pix"].append(pval)
        return json.dumps(jol, indent=4)
    
    def json_to_image(scling = 1, shrink = 1, json2 = '{"name": "lol", "w": 0, "h": 0, "pix":[[0,0,0],[]]}', output = 'img.png', rgb = color.rgb, r = color.r):
        js = json.loads(json2)
        img = Image.new(mode = 'RGB', size = (js["w"]*scling,js['h']*scling))
        scaling = (js["w"],js["h"])
        i = 0
        while i+shrink <= scaling[1]:
            for if3 in range(0,scling):
                i2 = 0
                while i2+shrink <= scaling[0]:
                    val = js["pix"][i][i2]
                    for if4 in range(0,scling):
                        img.putpixel( (i2*scling+if4,i*scling+if3) , (val[0],val[1],val[2], 255) )
                    i2 += shrink
            i += shrink
        img.save(output)


if __name__ == '__main__':
    import pathlib
    import sys
    if not len(sys.argv) > 1:
        exit
    x = ''
    #print(sys.argv, len(sys.argv))
    
    if len(sys.argv) > 2:
        for c in range(1,len(sys.argv)):
            x = x + sys.argv[c] + ' '
        x = x[:len(x)-1]
    x.replace('\\ ', ' ')
    x.replace('', ' ')
    print(x)
    x = 'c:\\Users\\Justus\\Documents\\CODE\\Python\\image to json\\images\\Merry Ficsmas 2021.PNG'
    #if pathlib.Path(x).is_file():
    ij2 = itj.img_to_json(1,50,str(x))
    # Automatic Down Scaling
    ij = json.loads(ij2)
    w = int(ij["w"])
    h = int(ij["h"])
    w2 = w
    h2 = h
    sc = 1
    while w2 > 38 or h2 > 38:
        sc += 1
        w2 = int(w/sc)
        h2 = int(h/sc)
    # Downscale
    mj = itj.manage_json(1,sc,ij2)
    # Display
    itj.json_to_text(1,1,mj)
    # Automatic Up Scaling
    ij = json.loads(mj)
    w = int(ij["w"])
    h = int(ij["h"])
    w2 = w
    h2 = h
    sc = 1
    while w2 < 500 or h2 < 500:
        sc += 1
        w2 = int(w*sc)
        h2 = int(h*sc)
    # Save to file
    itj.json_to_image(sc, 1, itj.manage_json(1,1,str(mj)))
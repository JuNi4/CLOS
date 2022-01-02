from PIL import Image
import json
import sys

class color():
    r = '\033[1;0m'
    def rgb(r=0,g=255,b=50):
        return '\033[38;2;'+str(r)+';'+str(g)+';'+str(b)+'m'

rgb = color.rgb
r = color.r

def img_to_text(scling = 1, shrink = 1, img = 'img.png'):
    scling = int(scling)
    shrink = int(shrink)
    img = Image.open(img)
    img = img.convert('RGB')
    scaling = img.getbbox()
    i = 0
    while i+shrink <= scaling[3]:
        i2 = 0
        pval = ''
        while i2+shrink <= scaling[2]:
            val = img.getpixel((i2,i))
            pval = pval+rgb(val[0], val[1], val[2])+'██'*scling
            i2 += shrink
        i += shrink
        print(pval+r)

if len(sys.argv) <= 1:
    print(rgb(150,10,10)+'specify path to img'+r)
else:
    c = 1
    arg = ''
    for o in range(1,len(sys.argv)):
        arg = arg+sys.argv[c]
        c += 1
    img_to_text(arg)
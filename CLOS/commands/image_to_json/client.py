import socket

def client(PORT = 4242):
    SERVER = "localhost"
    def sendMsg(MSG):
        # Socket erzeugen
        # Wir nutzen IPv4, TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (SERVER, PORT)

        # Verbindung aufbauen
        # TODO: Fehler-Auswertung fehlt!!!
        sock.connect(server_address)

        # Nachricht senden
        sock.sendall(MSG)

        # Verbindung wieder trennen
        sock.close()
        return 1

    # Hauptschleife
    c = 1
    arg = ''
    sar = sys.argv
    ext = ''
    if '-sc' in sar:
        ext = ext+' -sc '+sys.argv[sys.argv.index('-sc')+1]+' '
        sar.pop(sar.index('-sc')+1)
        sar.pop(sar.index('-sc'))
    if '-sh' in sar:
        ext = ext+' -sh '+sys.argv[sys.argv.index('-sh')+1]+' '
        sar.pop(sar.index('-sh')+1)
        sar.pop(sar.index('-sh'))
    for o in range(1,len(sar)):
        arg = arg+sar[c]+' '
        c += 1
    sendMsg(bytes(arg+ext,'utf-8'))

from PIL import Image

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
        #print(scling)
        #print(shrink)
        #print(i2, i)
        for i1 in range(0,scling):
            print(pval)

def client_server(scalimimg = 1):
    # "" == INADDR_ANY
    SERVER = ""
    PORT = 4242

    # Puffergroesse fuer recv()
    BUF_SIZE = 1024

    # Dies ist der Server.

    # Server-Port oeffnen
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (SERVER, PORT)

    # Server an den Port binden
    sock.bind(server_address)

    #print("Server arbeitet auf Port ", PORT, sep="")
    import os
    while True:
            # Receive response
            data, server = sock.recvfrom(4096)
            if data.decode() == 'cls ':
                os.system('cls')
            elif data.decode() == 'exit ':
                exit()
            else:
                scaling = "1"
                shrink = "1"
                msg = data.decode()
                if ' -sc ' in data.decode():
                    scaling = data.decode().split()[len(data.decode().split())-1]
                    msg = msg[0:len(msg)-len(' -sc '+scaling)]
                    msg = msg[:len(msg)-3]+msg[len(msg)-3:].replace(' ','')
                if ' -sh ' in data.decode():
                    shrink = data.decode().split()[len(data.decode().split())-1]
                    msg = msg[0:len(msg)-len(' -sh '+shrink)]
                    msg = msg[:len(msg)-3]+msg[len(msg)-3:].replace(' ','')
                img_to_text(int(scaling), int(shrink),msg)
import sys
if len(sys.argv) >= 2:
    if sys.argv[1] == 'd':
        client_server()
    else:
        client()
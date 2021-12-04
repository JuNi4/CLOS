# messenger -server -client -listserver

import threading
import datetime
import socket
import sys
import time

def client():
    arg = sys.argv
    if '-ip' in arg:
        SERVER = arg[arg.index('-ip')+1]
    else:
        print('ERROR: Server address needs to be defined (-ip [ip])')
        exit()
    if '-p' in arg:
        PORT = arg[arg.index('-p')+1]
    else:
        PORT = 4242

    if '-u' in arg:
        client_name = arg[arg.index('-u')+1]
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print('Warning, Username will be you IP: '+s.getsockname()[0])
        client_name = s.getsockname()[0]
        s.close()

    if not '-standalone' in arg:
        c_server = threading.Thread(target=client_server, args=())
        c_server.start()

    # Funktion, um die Nachricht "MSG" an den Server zu senden
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

    sendMsg(bytes('/join '+client_name, 'utf-8'))

    # Hauptschleife
    while True:
        mymsg = input("")
        sendMsg(bytes(mymsg, 'utf-8'))
        if mymsg[0:6] == '/leave':
            print('Leaving...')
            time.sleep(2)
            exit()


def client_server(ip = ""):
    # "" == INADDR_ANY
    SERVER = ip
    PORT = 4243

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

    while True:
            # Receive response
            data, server = sock.recvfrom(4096)
            if data.decode() == "!leave_account_requested_by_self":
                exit()
            print(data.decode())

def server(list_server_ip = '', list_server_port = '4244', server_name = '', server_port = '4242', listtheserver = False):
    print('---------------------------------------------')
    print(' JuNi\'s Messenger Server')
    print(' By JuNi, GitHub: https://github.com/juni4')
    print('---------------------------------------------')
    time.sleep(0.1)
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Starting server...")
    dev = False
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Debugmode "+str(dev))
    arg = sys.argv
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Arguments givin: "+str(arg))
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Setting PORT")
    PORT = int(server_port)
    # list server interaction
    #if '-lsip' in arg:
    #    lsip = arg[arg.index('-lsip')+1]
    # "" == INADDR_ANY
    SERVER = ""
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server listing: "+str(listtheserver))
    if not list_server_ip == '':
        print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] List Server IP: "+list_server_ip)
    if not list_server_port == '':
        print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] List Server Port: "+list_server_port)
    if bool(listtheserver):
        lspd = socket.socket()
        try:
            lspd.connect((list_server_ip, int(list_server_port)))
        except:
            print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] The Listserver is not available.")
            listtheserver = False

    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server NAME: "+server_name)

    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Setting up usr vars")
    usr = []
    usrn= []
    usraddr = []

    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Creating UDP Socket")
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Binding socket to PORT")
    # Bind the socket to the port
    server_address = (SERVER, PORT)
    #print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server opened on port: ", PORT, sep="")
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Done!")
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Awaiting Input...")
    while True:
        data, address = sock.recvfrom(4096)
        addr = address
        msg = data.decode()
        #print(str(addr)+': '+data.decode(), "'", sep="")
        if msg[0:5] == '/join':
            if not addr[0] in usr:
                name = msg[6:len(msg)]
                usr.append(str(addr[0]))
                usrn.append(name)
                usraddr.append(addr)
                print('['+datetime.datetime.now().strftime("%H:%M:%S")+'] New USER IP: '+str(addr[0])+' Name: '+name)
                for o in usr:
                    sock.sendto(bytes(usrn[usr.index(addr[0])]+" joined the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                    if dev:
                        print('Send join message to User Ip: '+o+' Name='+usrn[usr.index(o)])
            else:
                print('['+datetime.datetime.now().strftime("%H:%M:%S")+'] IP: '+addr[0]+' tried to login with a second account.')
        elif msg[0:6] == '/leave':
            usrindex = usr.index(addr[0])
            print('['+datetime.datetime.now().strftime("%H:%M:%S")+'] User with IP '+addr[0]+' and Name '+usrn[usr.index(addr[0])]+' left.')
            for o in usr:
                if o == addr[0]:
                    sock.sendto(bytes("!leave_account_requested_by_self", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                else:
                    sock.sendto(bytes(usrn[usr.index(addr[0])]+" left the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                if dev:
                    print('Send leave message to User Ip: '+o+' Name='+usrn[usr.index(o)])
            usr.pop(int(usrindex))
            usrn.pop(int(usrindex))
            usraddr.pop(int(usrindex))
        elif msg[0:5] == '/list':
            user_list = ''
            c = 0
            for o in usrn:
                if user_list == '':
                    user_list = user_list +'' + usrn[c]
                else:
                    user_list = user_list +', ' + usrn[c]
                c += 1
            if len(usr) == 1:
                lmsg ="There is "+str(len(usr))+" person in the room: "+user_list
            else:
                lmsg = lmsg ="There are "+str(len(usr))+" persons in the room: "+user_list
            print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] [Server] "+lmsg)
            for o in usr:
                sock.sendto(bytes(lmsg, encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                if dev:
                    print('Send userlist to User Ip: '+o+' Name='+usrn[usr.index(o)])
        elif addr[0] in usr:
            print('['+datetime.datetime.now().strftime("%H:%M:%S")+'] <'+usrn[usr.index(str(addr[0]))]+'> '+msg)
            retmsg = '<'+usrn[usr.index(str(addr[0]))]+'> '+msg
            for o in usr:
                if not o == addr[0]:
                    sock.sendto(bytes(retmsg, encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                    if dev:
                        print('Send message to User Ip: '+o+' Name='+usrn[usr.index(o)])
                #strdata = data.decode()
                #retmsg = '<'+usrn[usr.index(str(addr[0]))]+'> '+msg + strdata
                #con.sendall(retmsg.encode())


def list_servers_server():
    # "" == INADDR_ANY
    SERVER = ""
    PORT = 4242

    # Puffergroesse fuer recv()
    BUF_SIZE = 1024

    # Dies ist der Server.

    # Server-Port oeffnen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER, PORT)

    # Server an den Port binden
    sock.bind(server_address)

    print("Server arbeitet auf Port ", PORT, sep="")

    sock.listen()

    while True:
        print("Warte auf Verdindung ...")
        con, addr = sock.accept()

        # con ist ein neuer Socket, der speziell fuer diese Verbindung
        # erstellt wurde.

        print("Neue Verbidnung von ", addr)

        con_active = 1

        while (1 == con_active):
            # Daten empfangen
            data = con.recv(BUF_SIZE)
            # Wenn nicht leer, ausgeben
            if data:
                # print("Empfangen: '", data.decode(), "'", sep="")
                # Antwort erzeugen und zuruecksenden
                strdata = data.decode()
                retmsg = "Antwort: " + strdata
                con.sendall(retmsg.encode())
            else:
                # recv kehr ohne Daten zurueck-> Fehler ist aufgetreten
                # Verbindung wurde beendet
                con.close()
                con_active = 0

def log(log_string):
    print()

def getarg(arg, alt):
    if not arg == '':
        if arg in sys.argv:
            return sys.argv[sys.argv.index(arg)+1]
        else: return alt

arg = sys.argv
if '-s' in arg or '-server' in arg[1] or arg[1] == ' server ':
    if '-h' in arg:
        print('HELP: \n -h  Help\n -name  Server Name\n -p  Server Port\n -lsip  IP of List Server\n -lsp  Port of List Server\n -els  Enable the list server')
        exit()
    server(list_server_ip=getarg('-lsip', 'localhost'), list_server_port=getarg('-lsp', '4244'), server_name=getarg('-name', ''), server_port=getarg('-p', '4242'), listtheserver=getarg('-els', False))
if '-c' in arg or '-client' in arg[1] or arg[1] == ' client ':
    client()
if '-ls' in arg or '-listserver' in arg or arg[1] == ' listserver ':
    client()
if '-cs' in arg or '-clientserver' in arg or arg[1] == ' clientserver ':
    client_server()
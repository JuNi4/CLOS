# messenger -server -client -listserver

import threading
import platform
import datetime
import socket
import sys
import os
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
        c_server = threading.Thread(target=client_server, args=('', str(os.getpid())))
        c_server.start()

    pw = getarg('-pw', '')

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

    if not pw == '':
        sendMsg(bytes('/auth '+pw, 'utf-8'))
    sendMsg(bytes('/join '+client_name, 'utf-8'))

    # Hauptschleife
    while True:
        mymsg = input("")
        sendMsg(bytes(mymsg, 'utf-8'))
        if mymsg[0:6] == '/leave':
            print('Leaving...')
            time.sleep(2)
            exit()


def client_server(ip = "", cpid = ''):
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
            if data.decode()[0:32] == "!leave_account_requested_by_self":
                if data.decode() == "!leave_account_requested_by_self _nonself":
                    print('You got kicked!')
                    if 'Windows' in platform.system():
                        os.system('taskkill /PID '+cpid+' /F')
                    else:
                        os.system('kill '+cpid)
                    time.sleep(2)
                exit()
            print(data.decode())

def server(list_server_ip = '', list_server_port = '4244', server_name = '', server_port = '4242', listtheserver = False, ch_log = '', l_file = '', epw = False, pw ='', apw = 'jf/eu§nf(7UF+3ef5#]534*', ecl = True):
    log('\n\nlog from '+"--"+datetime.datetime.now().strftime("%Y/%m/%D %H:%M:%S")+"--\n", l_file, False)
    log('---------------------------------------------', l_file)
    log(' JuNi\'s Messenger Server', l_file)
    log(' By JuNi, GitHub: https://github.com/juni4', l_file)
    log('---------------------------------------------', l_file)
    time.sleep(0.1)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Starting server...", l_file)
    dev = False
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Debugmode "+str(dev), l_file)
    arg = sys.argv
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Arguments givin: "+str(arg), l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Setting PORT", l_file)
    PORT = int(server_port)
    # list server interaction
    #if '-lsip' in arg:
    #    lsip = arg[arg.index('-lsip')+1]
    # "" == INADDR_ANY
    SERVER = ""
    # List server stuff
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server NAME: "+server_name, l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server Pssword: "+str(epw), l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server listing: "+str(listtheserver), l_file)
    if not list_server_ip == '':
        log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] List Server IP: "+list_server_ip, l_file)
    if not list_server_port == '':
        log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] List Server Port: "+list_server_port, l_file)
    if bool(listtheserver):
        lspd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            lspd.connect((list_server_ip, int(list_server_port)))
            lspd.close()

            log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Getting PC IP.", l_file)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            cserver_ip = s.getsockname()[0]
            s.close()

            log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Rigistering Server on List Server as "+server_name+".", l_file)

            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(bytes('list_register '+cserver_ip+' '+str(PORT)+' '+server_name+' '+str(epw)+' 0','utf-8'), (list_server_ip, int(list_server_port)))
                sock.close()
                log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server Registered.", l_file)
            except:
                log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Register Error. Maybe the server is offline?", l_file)

        except:
            log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] The Listserver is not available.", l_file)
            listtheserver = False
            lspd.close()

    

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Setting up usr vars", l_file)
    usr = []
    usrn= []
    usraddr = []
    auth = []
    admin_auth = []
    waitlistn = []
    waitlistip = []

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Creating UDP Socket", l_file)
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Binding socket to PORT", l_file)
    # Bind the socket to the port
    server_address = (SERVER, PORT)
    #log('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server opened on port: "+ str(PORT), l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Done!", l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Awaiting Input...", l_file)
    while True:
        data, address = sock.recvfrom(4096)
        addr = address
        msg = data.decode()
        #log(str(addr)+': '+data.decode(), "'", sep="")
        # Join server
        if msg[0:5] == '/join':
            # If user is permitted to join...
            if addr[0] in auth or epw == False:
                # ..and not already connected...
                if not addr[0] in usr:
                    # ..let USR join
                    # set name of usr
                    name = msg[6:len(msg)]
                    # add usr values to joined list
                    usr.append(str(addr[0]))
                    usrn.append(name)
                    usraddr.append(addr)
                    # tell other users that a new usr joined
                    log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] New USER IP: '+str(addr[0])+' Name: '+name, l_file)
                    for o in usr:
                        sock.sendto(bytes(usrn[usr.index(addr[0])]+" joined the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                        if ecl:
                            log(usrn[usr.index(addr[0])]+" joined the room.",ch_log, False)
                        #log(,ch_log, False)
                        if dev:
                            log('Send join message to User Ip: '+o+' Name='+usrn[usr.index(o)], l_file)
                else:
                    log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] IP: '+addr[0]+' tried to login with a second account.', l_file)
            else:
                name = msg[6:len(msg)]
                waitlistn.append(name)
                waitlistip.append(addr[0])

        # Auth on Server
        elif msg[0:5] == '/auth' and epw:
            if msg[6:len(msg)] == pw:
                auth.append(addr[0])
            if not addr[0] in usr:
                # ..let USR join
                # set name of usr
                name = waitlistn[waitlistip.index(addr)]
                # add usr values to joined list
                usr.append(str(addr[0]))
                usrn.append(name)
                usraddr.append(addr)
                # tell other users that a new usr joined
                log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] New USER IP: '+str(addr[0])+' Name: '+name, l_file)
                for o in usr:
                    sock.sendto(bytes(usrn[usr.index(addr[0])]+" joined the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                    #log(,ch_log, False)
                    if dev:
                        log('Send join message to User Ip: '+o+' Name='+usrn[usr.index(o)])
                if ecl:
                    log(usrn[usr.index(addr[0])]+" joined the room.",ch_log, False)
        # Admin auth on Server
        elif msg[0:6] == '/aauth':
            if msg[7:len(msg)] == apw:
                log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] USER IP: '+str(addr[0])+' Name: '+usrn[usr.index(addr[0])]+' became mod.', l_file)
                admin_auth.append(addr[0])
                for o in admin_auth:
                    sock.sendto(bytes(usrn[usr.index(addr[0])]+" became mod.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                    if dev:
                        log('Send mod message to User Ip: '+o+' Name='+usrn[usr.index(o)],l_file)
        # /leave command
        elif msg[0:6] == '/leave':
            # get usr index in usr list
            usrindex = usr.index(addr[0])
            # log message that usr xy left
            log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] User with IP '+addr[0]+' and Name '+usrn[usr.index(addr[0])]+' left.', l_file)
            if ecl:
                log(usrn[usr.index(addr[0])]+" left the room.",ch_log, False)
            # send all usrs leave message
            for o in usr:
                if o == addr[0]:
                    # if its the person who want's to leave, send the cs a exit message
                    sock.sendto(bytes("!leave_account_requested_by_self", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                else:
                    # else send leave message
                    sock.sendto(bytes(usrn[usr.index(addr[0])]+" left the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                    
                if dev:
                    # debug mesage
                    log('Send leave message to User Ip: '+o+' Name='+usrn[usr.index(o)])
            if epw:
                auth.pop(int(usrindex))
            # remove usr from admin list
            if addr[0] in admin_auth:
                admin_auth.pop(usrindex)
             # remove usr from usr lists
            usr.pop(int(usrindex))
            usrn.pop(int(usrindex))
            usraddr.pop(int(usrindex))
            # remove usr from auth list
        # list command
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
            log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] [Server] "+lmsg, l_file)
            for o in usr:
                if ecl:
                    log(lmsg,ch_log, False)
                sock.sendto(bytes(lmsg, encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                if dev:
                    log('Send userlist to User Ip: '+o+' Name='+usrn[usr.index(o)])
        # Admin commands
        elif msg[0:1] == '!':
            def ac(c,istr, ofs = 0, low = True):
                if low:
                    istr = istr[ofs:len(c)].lower()
                    c = c.lower()
                else:
                    istr = istr[ofs:len(c)]
                    c = c
                if istr == c:
                    return True
                else:
                    return False
            if addr[0] in admin_auth :
                if ac('!help',msg, low = False):
                    hmsg = ' !help  Shows this message\n !chatlog_clear  Clears the chat log - the log wich is send to a user on join\n !chatlog_dis  Diables the chat log and it will no longer be send to usrs on join\n !chatlog_en  Enables the chatlog and all writen messages will be send to joining usrs\n !kick  Kicks the Person (usrname)'
                    sock.sendto(bytes(hmsg, encoding='utf-8'), (addr[0],4243))
                if ac('!chatlog_clear',msg):
                    f = open(ch_log, 'w')
                    f.write('')
                    f.close()
                if ac('!chatlog_en',msg):
                    ecl = True
                if ac('!chatlog_dis',msg):
                    ecl = False
                if ac('!kick',msg):
                    # get usr index in usr list
                    usrindex = usrn.index(msg[6:len(msg)])
                    # log message that usr xy left
                    log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] User with IP '+addr[0]+' and Name '+usrn[usr.index(addr[0])]+' got kicked by '+usrn[usr.index(addr[0])]+'.', l_file)
                    if ecl:
                        log(usrn[usr.index(addr[0])]+" left the room.",ch_log, False)
                    # send all usrs leave message
                    for o in usr:
                        if usrn[usr.index(o)] == msg[6:len(msg)]:
                            # if its the person who want's to leave, send the cs a exit message
                            sock.sendto(bytes("!leave_account_requested_by_self _nonself", encoding='utf-8'), (usraddr[usrn.index(msg[6:len(msg)])][0],4243))
                        else:
                            if o in admin_auth:
                                sock.sendto(bytes(usrn[usrn.index(msg[6:len(msg)])]+" got kicked by "+usrn[usr.index(addr[0])]+'.', encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                            else:
                                # else send leave message
                                sock.sendto(bytes(usrn[usrn.index(msg[6:len(msg)])]+" left the room.", encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                                
                        if dev:
                            # debug mesage
                            log('Send leave message to User Ip: '+o+' Name='+usrn[usr.index(o)])
                    # remove usr from auth list
                    if epw:
                        auth.pop(int(usrindex))
                    # remove usr from admin list
                    if usr[usrindex] in admin_auth:
                        admin_auth.pop(usrindex)
                    # remove usr from usr lists
                    usr.pop(int(usrindex))
                    usrn.pop(int(usrindex))
                    usraddr.pop(int(usrindex))
                    
            else:
                sock.sendto(bytes('Error: You are not permitted to do that!', encoding='utf-8'), (addr[0],4243))
                log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] Error: USR '+usrn[usr.index(addr[0])]+' tried to execute Admin Commands while not authed', l_file)
        elif addr[0] == list_server_ip and msg == '_Still Active dude?':
            time.sleep(0.1)
            log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] List Server Ping',l_file)
            sock.sendto(bytes('list_update '+cserver_ip+' '+str(PORT)+' '+server_name+' '+str(epw)+' '+str(len(usr)),'utf-8'), (list_server_ip, int(list_server_port)))
        elif addr[0] in usr:
            if addr[0] in auth or epw == False:
                log('['+datetime.datetime.now().strftime("%H:%M:%S")+'] <'+usrn[usr.index(str(addr[0]))]+'> '+msg, l_file)
                retmsg = '<'+usrn[usr.index(str(addr[0]))]+'> '+msg
                for o in usr:
                    if not o == addr[0]:
                        sock.sendto(bytes(retmsg, encoding='utf-8'), (usraddr[usr.index(o)][0],4243))
                        if ecl:
                            log(retmsg,ch_log, False)
                        if dev:
                            log('Send message to User Ip: '+o+' Name='+usrn[usr.index(o)], l_file)
                    #strdata = data.decode()
                    #retmsg = '<'+usrn[usr.index(str(addr[0]))]+'> '+msg + strdata
                    #con.sendall(retmsg.encode())



def list_servers_server(ip = '', PORT = '', log_file = ''):
    dev = False

    if log_file == '':
        l_file = os.path.dirname(os.path.realpath(__file__))+'\\list_server_log.txt'
    else:
        l_file = log_file
    log('\n\nlog from '+"--"+datetime.datetime.now().strftime("%Y/%m/%D %H:%M:%S")+"--\n", l_file, False)
    log('---------------------------------------------', l_file)
    log(' JuNi\'s Messenger List Server', l_file)
    log(' By JuNi, GitHub: https://github.com/juni4', l_file)
    log('---------------------------------------------', l_file)
    time.sleep(0.1)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Starting server...", l_file)
    dev = False
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Debugmode "+str(dev), l_file)

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Setting up server vars", l_file)
    SERVER = ""
    reg_servers_ip = []
    reg_servers_p = []
    reg_servers_name = []
    reg_servers_epw = []
    reg_servers_uc = []

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Creating UDP Socket", l_file)
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Binding socket to PORT", l_file)
    # Bind the socket to the port
    server_address = (SERVER, int(PORT))
    #print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server opened on port: "+ PORT, l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Done!", l_file)
    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Awaiting Input...", l_file)
    while True:
        data, address = sock.recvfrom(4096)
        addr = address
        msg = data.decode()
        #print(str(addr)+': '+data.decode(), "'", sep="")
        # refresh server list
        c = 0
        for o in reg_servers_ip:
            try:
                sock.sendto(bytes('_Still Active dude?', encoding='utf-8'), (o,int(reg_servers_p[c])))
                data2, address = sock.recvfrom(4096)
                addr2 = address
                msg2 = data2.decode()
                larg = msg2.split(' ')
                if larg[0] == 'list_update':
                    reg_servers_ip[c] = larg[1]
                    reg_servers_name[c] = larg[3]
                    reg_servers_p[c] = larg[2]
                    reg_servers_epw[c] = larg[4]
                    reg_servers_uc[c] = larg[5]
                    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server with Name "+reg_servers_name[c]+" and IP "+reg_servers_ip[c]+" is stil Active.", l_file)
                else:
                    log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server with Name "+reg_servers_name[c]+" and IP "+reg_servers_ip[c]+" is inactive and will be removed from Serverlist.", l_file)
                    reg_servers_ip.pop(c)
                    reg_servers_name.pop(c)
                    reg_servers_p.pop(c)
                    reg_servers_epw.pop(c)
                    reg_servers_uc.pop(c)
                #lspd.connect((reg_servers_ip[c], int(reg_servers_p[c])))
            except:
                log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Server with Name "+reg_servers_name[c]+" and IP "+reg_servers_ip[c]+" is inactive and will be removed from Serverlist.", l_file)
                reg_servers_ip.pop(c)
                reg_servers_name.pop(c)
                reg_servers_p.pop(c)
                reg_servers_epw.pop(c)
                reg_servers_uc.pop(c)
            c += 0
        log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Refreshed server list.", l_file)
        if msg[0:13] == 'list_register':
            larg = msg.split(' ')
            #print(msg)
            log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Added New Server, IP: "+larg[1]+' Port: '+larg[2]+' Name: '+larg[3]+'.', l_file)
            reg_servers_ip.append(larg[1])
            reg_servers_name.append(larg[3])
            reg_servers_p.append(larg[2])
            reg_servers_epw.append(larg[4])
            reg_servers_uc.append(larg[5])
            #print(reg_servers_ip,reg_servers_epw)
            
        elif msg[0:5] == '/list':
            sock.sendto(bytes('All known Servers:', encoding='utf-8'), (addr[0],4243))
            sock.sendto(bytes(' Name:        IP:              Port:      PW(Y/N):   USR:', encoding='utf-8'), (addr[0],4245))
            c = 0
            for o in reg_servers_ip:
                sn = 12-len(reg_servers_name[c])
                sip =17-len(reg_servers_ip[c])
                sp = 8-len(reg_servers_p)
                sn2 = ' '*sn
                sip2= ' '*sip
                if reg_servers_epw[c] == 'True':
                    pwq = 'Y'
                else:
                    pwq = 'N'
                sock.sendto(bytes('  '+reg_servers_name[c]+sn2+reg_servers_ip[c]+sip2+reg_servers_p[c]+' '*sp+pwq+' '*10+reg_servers_uc[c], encoding='utf-8'), (addr[0],4245))
                c += 1
            sock.sendto(bytes('!system_message:end', encoding='utf-8'), (addr[0],4245))
            if dev:
                log("["+datetime.datetime.now().strftime("%H:%M:%S")+'] Send serverlist to User Ip: '+o+' Name='+addr[0], l_file)
        elif msg[0:5] == '/join':
            sock.sendto(bytes("!leave_account_requested_by_self", encoding='utf-8'), (addr[0],4243))

# log and print 
def log(log_string, log_file, o = True):
    if o:
        print(log_string)
    f = open(log_file, 'a')
    f.write(log_string+'\n')
    f.close()

# get -xyz arg in sys.argv
def getarg(arg, alt):
    if not arg == '':
        if arg in sys.argv:
            return sys.argv[sys.argv.index(arg)+1]
        else: return alt

arg = sys.argv
# launch correct 'apllication'
if len(arg) > 1:
    # Server launcher
    if '-s' in arg or '-server' in arg[1] or arg[1] == ' server ':
        # help
        if '-h' in arg:
            print('HELP: \n -h  Help\n -name  Server Name\n -p  Server Port\n -lsip  IP of List Server\n -lsp  Port of List Server\n -els  Enable the list server\n -pw  Password for Server')
            exit()
        if '-els' in arg:
            els = True
        else:
            els = False
        if '-pw' in arg:
            epw = True
        else:
            epw = False
        if '-ecl' in arg:
            ecl = True
        else:
            ecl = False
        server(list_server_ip=getarg('-lsip', 'localhost'), list_server_port=getarg('-lsp', '4244'), server_name=getarg('-name', ''), server_port=getarg('-p', '4242'), listtheserver=els, l_file=getarg('-lf', os.path.dirname(os.path.realpath(__file__))+'\\messenger_server_log.txt'), ch_log=getarg('-cl', os.path.dirname(os.path.realpath(__file__))+'\\messenger_chat_log.txt'), ecl=ecl, apw=getarg('-apw','jf/eu§nf(7UF+3ef5#]534*'), epw = epw, pw = getarg('-pw', ''))
    # Client launcher
    if '-c' in arg or '-client' in arg[1] or arg[1] == ' client ':
        client()
    # List Server launcher
    if '-ls' in arg or '-listserver' in arg or arg[1] == ' listserver ':
        list_servers_server(PORT = getarg('-p', '4244'), log_file=getarg('-lf', ''))
    # Client Server Launcher - For Split Sending & Reciveving messages
    if '-cs' in arg or '-clientserver' in arg or arg[1] == ' clientserver ':
        client_server()
    # list servers from list server
    if 'list' in arg:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("/list", encoding='utf-8'), (getarg('-ip', 'localhost'),int(getarg('-p', '4244'))))
        sock.close()
        # ip and port for list server
        SERVER = ""
        PORT = 4245

        # Puffergroesse fuer recv()
        BUF_SIZE = 1024

        # Dies ist der Server.

        # Server-Port oeffnen
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (SERVER, int(PORT))

        # Server an den Port binden
        x = True
        sock.bind(server_address)
        while x:
            data, server = sock.recvfrom(4096)
            if data.decode() == '!system_message:end':
                x = False
            else:
                print(data.decode())
        exit()

print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] LOL.")
input()
#log("["+datetime.datetime.now().strftime("%H:%M:%S")+"] .", l_file)
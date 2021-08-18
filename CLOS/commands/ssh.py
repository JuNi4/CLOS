# SSH Client & Server
import socket
import sys
import time

def client():
    SERVER = input(str("Please enter the host address of the sender : "))
    PORT = 4242


    # Funktion, um die Nachricht "MSG" an den Server zu senden
    def sendMsg(MSG):
        # Socket erzeugen
        # Wir nutzen IPv4, TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    while True:
        mymsg = bytes(input(), 'utf-8')
        sendMsg(mymsg)

def server():
    # "" == INADDR_ANY
    SERVER = ""
    PORT = 4242
    
    # Puffergröße für recv()
    BUF_SIZE = 1024
    
    # Dies ist der Server.
    
    # Server-Port öffnen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER, PORT)
    
    # Server an den Port binden
    sock.bind(server_address)
    
    print("Server arbeitet auf Port ", PORT, sep="")
    
    sock.listen()
    
    while True:
        print("Warte auf Verdindung ...")
        con, addr = sock.accept()
    
        # con ist ein neuer Socket, der speziell für diese Verbindung
        # erstellt wurde.
    
        print("Neue Verbidnung von ", addr)
    
        con_active = 1
        
        while (1 == con_active):
            # Daten empfangen
            data = con.recv(BUF_SIZE)
            # Wenn nicht leer, ausgeben
            if data:
                print("Empfangen: '", data.decode(), "'", sep="")
                # Antwort erzeugen und zurücksenden
                strdata = data.decode()
                retmsg = "Antwort: "+ strdata
                con.sendall(retmsg.encode())
            else:
                # recv kehr ohne Daten zurück-> Fehler ist aufgetreten
                # Verbindung wurde beendet
                print("Verbindung getrennt!")
                con.close()
                con_active = 0
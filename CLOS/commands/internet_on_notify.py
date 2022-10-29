import http.client as httplib
from datetime import datetime
from pythonping import ping
import time
import os

# Path of alert
alert = 'D:\Justus\Videos\\4K Video Downloader\karlson vibe [epilepsy warning] (perfect loop).mp4'

def internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

x = 1
x2 = 0
alert = '"'+alert+'"'

while True:
    if internet() == True:
        x = 1
        if x2 == 1:
            print('Currently There Is No Connection With The Internet Since '+str(start_time)+' for '+str(hui)+'m '+str(mrf)[:2]+'s.         ')
            os.system(alert)
        x2 = 0
        response_list = ping('google.com', size=40, count=4)
        ms = str(response_list.rtt_avg_ms)
        print('Currently Your Connected To The Internet With A Ping Of '+ms+'ms.                   ', end='\r')
        
    else:
        if x == 1:
            print('Currently Your Connected To The Internet With A Ping Of '+ms+'ms.                   ')
            time_time = datetime.now()
            start_time = time_time.strftime("%Hh %Mm %Ss")
            starttime = time.time()
        x = 0 
        x2 = 1
        endtime = time.time()
        inp = endtime - starttime
        hui = int(inp/60)
        mrc = hui*60
        mrf = inp - mrc
        print('Currently There Is No Connection With The Internet Since '+str(start_time)+' for '+str(hui)+'m '+str(mrf)[:2]+'s.         ',end='\r')

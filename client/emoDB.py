#########################################
# EmoDB Database Client
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################
from dummy_threading import Thread
import socket
import argparse
import threading
import sys

ap = argparse.ArgumentParser()
ap.add_argument('-ip', help="link to a ipaddress the server running on", required=True)
ap.add_argument('-p', '--port', help="link to a port the server running on", required=True)
# ap.add_argument('-db', '--dbpath', help="set a path to save databases", required=True)
ap.add_argument('-u', help="the user you will use",required=True)
ap.add_argument('-vc', help="the verification code for the user",required=True)
args = ap.parse_args()
s=socket.socket()

s.connect((args.ip,int(args.port)))

def ushow():
    while 1:
        print(s.recv(1024).decode(encoding="utf8"))

thread = Thread(target=ushow)
thread.setDaemon(True)
comd = input(">")

if(comd == "exit"):
    sys.exit()

s.send(comd.encode('utf8'))

while 1:
    # if len(s.recv(1024).decode(encoding="utf8")) == 0:
    #     pass
    # print(s.recv(1024).decode(encoding="utf8"))
    comd = input(">")

    if(comd == "exit"):
        sys.exit()

    s.send(comd.encode('utf8'))
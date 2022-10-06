#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################
from asyncio.windows_events import NULL
import os
from re import T
import sys
import argparse
import time
import pathlib
from datetime import date
import logging
import os

ap = argparse.ArgumentParser()

ap.add_argument('-p', '--port', help="set a port the server running on", required=True)
ap.add_argument('-db', '--dbpath', help="set a path to save databases", required=True)


args = ap.parse_args()
# 添加封装库
sys.path.append(".")

from emodb import eSocket
from emodb import edbLog
from emodb import eInit
from emodb import eSecurity
from emodb import eControlDB

fpth = os.path.dirname(__file__)+"\\log"+"\\"+time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())+".log"

if pathlib.Path(os.getcwd()+"\\log").exists():
    pass
else:
    os.mkdir(os.getcwd()+"\\log")

eInit.cDBdir(args.dbpath)
eControlDB.eInitCtrlDB(args.dbpath)

# os.system("echo >"+fpth)
eSocket.cSocket(int(args.port))

edbLog.rLogs("info","Server is running\n",fpth)

while True:
    pass
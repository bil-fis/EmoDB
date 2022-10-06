#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################

from datetime import date
import os
import time
import sys

def rLogs(loLevel,loMessage,filepath):
    with open(filepath,'a+') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"  "+sys.argv[0]+" ["+loLevel+"]"+loMessage)

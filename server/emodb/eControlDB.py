#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################
import os

dplist = []

def eInitCtrlDB(dbdir):
    global dplist
    for dbs in os.listdir(dbdir):
        dplist.append(dbs)

def getDB():
    print(dplist)
    return dplist
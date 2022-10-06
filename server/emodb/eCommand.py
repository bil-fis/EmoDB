#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################

from emodb import eControlDB
import json

def eCommands(comd):
    eComd = comd.split()[0]
    if (eComd == "gtdb"):
        ebkc = json.dumps(eControlDB.getDB().__dict__)
        return ebkc
    else:
        ebkc = json.dumps('{"id":"-1", "msg": "operate command invaild"}')
        print(ebkc)
        return ebkc
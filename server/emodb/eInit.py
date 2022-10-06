#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################

import pathlib
import os
import random
import string
import hashlib

def cDBdir(dbdir):
    if pathlib.Path(dbdir).exists():
        pass
    else:
        os.mkdir(dbdir)

    if pathlib.Path(dbdir+"\\.installed").exists():
        pass
    else:
        with open(dbdir+"\\.installed",'a+') as f:
            prot = ''.join(random.choice(string.ascii_letters + "0123456789~!@#$%^&*()_+`-=") for x in range(1024))
            f.write(prot)
            f.close()
        # ran_ustr = random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789+-*/><?}{]|',15)
        # ran_pstr = random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789+-*/><?}{]|',15)
        # print("[IMPORTANT] username:"+ran_ustr+"  password:"+ran_pstr+"\n this will show once, please write them down")

        char = string.ascii_letters + "0123456789~!@#$%^&*()_+`-="
        uname = ''.join(random.choice(char) for x in range(12))

        pname = hashlib.md5(''.join(random.choice(char) for x in range(128)).encode(encoding='utf8')).hexdigest()

        print("User Name: "+uname)
        print("Security Code: "+pname)
        print("[INFO] Above infomation will not show again.\n")
        
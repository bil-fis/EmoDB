#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################

from secrets import token_bytes
import pathlib
from pathlib import Path
import emodb.edbLog

exStr = "genshinnahida213330626#$#@%#$@!&^#*@#&*~&*@~"

def rKeys():
    global exStr
    key = token_bytes(nbytes=1024)
    key_int = int.from_bytes(key,exStr)
    return key_int

def encrypt(raw,exStr):
    raw_bytes = raw.encode()
    raw_int = int.from_bytes(raw_bytes, exStr)
    key_int = rKeys(len)

def eEncrypt(path,key_path=None,*,encoding='utf-8'):
    path = Path(path)
    cwd = path.cwd() / path.name.split('.')[0]
    path_encrypted = cwd / path.name
    if key_path is None:
        key_path = cwd / '.installed'
    if not cwd.exists():
        cwd.mkdir()
        path_encrypted.touch()
        key_path.touch()

    with path.open('rt', encoding=encoding) as f1, \
        path_encrypted.open('wt', encoding=encoding) as f2, \
            key_path.open('wt',encoding=encoding) as f3:
        
        encrypted,key = rKeys(f1.read())
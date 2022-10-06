#########################################
# EmoDB Database Server
# author: bil_fis
# 
# 
# Do not use it for business.
#########################################
import socket
from threading import Thread
from emodb import eCommand

sk = None
conpool = []  # 连接池
    
def cSocket(port):
    global sk
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        severip = ('127.0.0.1',port)
        sk.bind(severip)
        sk.listen(5)
    except:
        print("[Warn] Cannot start server")
    print("[OK]Server is running on ",port,", waiting for any connections...")
    thread = Thread(target=wClient)
    thread.setDaemon(True)
    thread.start()

def mHandle(client):
    print("[INFO] A client connected, id",client)
    nClient = conpool.index(client)
    conpool[nClient].sendall("v1".encode(encoding="utf8"))
    print("client id: "+str(nClient))
    while True:
        
        bytes = client.recv(1024)
        print("[MSG] Got client message:", bytes.decode(encoding="utf8"))
        # print("ebkc return: "+eCommand.eCommands(bytes.decode(encoding="utf8")))
        # conpool[nClient].sendall(eCommand.eCommands(bytes.decode(encoding="utf8")).encode(encoding='utf8'))

        try:
            bytes = client.recv(1024)
            print("[MSG] Got client message:", bytes.decode(encoding="utf8"))
            # ebkc = eCommand.eCommands(bytes.decode(encoding="utf8"))

            # print("ebkc return: "+eCommand.eCommands(bytes.decode(encoding="utf8")))

            conpool[nClient].sendall(str(eCommand.eCommands(bytes.decode(encoding="utf8"))).encode(encoding='utf8'))
        except TypeError as e:
            print(e)
        except:
            client.close()
            conpool.remove(client)
            print("[INFO] Client disconnected")
            break

        if len(bytes) == 0:
            client.close()
            conpool.remove(client)
            print("[INFO] A client disconnected")
            break

def wClient():
    while 1:
        client, _ = sk.accept()
        conpool.append(client)
        thread = Thread(target=mHandle, args=(client,))
        thread.setDaemon(True)
        thread.start()

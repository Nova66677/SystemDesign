import socket
import threading


host = "127.0.0.1"
port = 4444

def my_func(t, addr):
    contenu = t.recv(4096).decode()
    print(str(addr[0]), "> ", contenu)
    print("Goodbye ! ")
    t.send(b'Message recu !')
    t.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Waiting for incoming connections...")

i = 0
# On lance notre boucle qui attend des connections
while i < 5 :
    s.listen(5)
    c, addr = s.accept()
    threading.Thread(target=my_func, args=(c,addr)).start()
    i += 1

s.close()





import socket
import threading


host = "127.0.0.1"
port = 4444

def my_func(c, addr):
    """
    :param c: (object socket) notre connection fille entre le serveur et le client
    :param addr: (tuple) Contient l'adresse et le port de notre connection fille
    :return: None
    """
    contenu = c.recv(4096).decode()
    print(str(addr[0]), "> ", contenu)
    print("Goodbye ! ")
    c.send(b'Message recu !')
    c.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Waiting for incoming connections...")

i = 0
# On lance notre boucle qui attend des connections
while i < 5 :
    s.listen(5)
    c, addr = s.accept()
    threading.Thread(target=my_func, args=(c,addr)).start() # On créé notre thread qui gère le client arrivé
    i += 1

s.close() # On ferme la connection principale





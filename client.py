import socket

host = "127.0.0.1"
port = 4444

print("Connecting to target...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connection successfull !")
s.send(b'coucou')
contenu = s.recv(2048).decode()
print(contenu)
s.close()




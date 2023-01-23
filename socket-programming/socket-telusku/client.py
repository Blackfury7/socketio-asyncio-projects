import socket

c = socket.socket()

c.connect(('localhost', 9999))

# print((c.recv(1024)))
print((c.recv(1024).decode()))
while True:

    msg = input()
    c.send(bytes(msg,'utf-8'))
    c.close

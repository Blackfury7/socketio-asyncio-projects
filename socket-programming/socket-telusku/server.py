import socket 

s= socket.socket()
print('Socket Created')

s.bind(
    ('localhost',9999)
)



while True:
    s.listen(3)
    print('waiting for connections')
    c, addr = s.accept()
    print("Connected with ", addr)

    # c.send(bytes('Welcome to Socket', 'utf-8'))
    # msg_recieved = c.recv(1024).decode()
    c.close()
import socket
s = socket.socket()
host = ('ip here')
port = 22
s.bind((host,port))
print ("server started on:\n*",host,":",port)
s.listen(5)
x = 0
c, addr = s.accept()
print ('Got connection from',addr)
print (c.recv(4096))
if c.recv == "test":
        print ("good")
while x < 956000:
        print (c.recv(4096))
        message = input ("Message to send:")
        s.sendall(message.encode('utf-8')),(addr[0], addr[1])
        print(s.recv(1024))

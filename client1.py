import socket
import polynomials

#socket()
sock=socket.socket()

#connect()
sock.connect(('127.0.0.1', 12345))
#write()


request=input("Please enter polynomial: ")


sock.sendall(request.encode())
sock.shutdown(1)    # signal the server we're sending no more data

bytes=sock.recv(2048)
response=""

while len(bytes)>0:
    response+=bytes.decode()
    bytes = sock.recv(2048)

print(response)

sock.close()

#read()

#close()
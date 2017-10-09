
import socket
import logging
import polynomals

port=12345

logging.basicConfig(level=logging.ERROR)

#socket()
listener=socket.socket()
#bind(): Ip address with port number
listener.bind(('127.0.0.1',port))
#listen()
listener.listen(0)
#accept()

while True:
    (sock,addr)=listener.accept()  ## waits for a connection request
                                    # when successful, returns a socket
                                    # to use to communicate with the client
    #read()
    logging.debug("Server connected to:"+str(addr))
    bytes=sock.recv(2048)

    client_data=""
    # get data from the client
    while len(bytes)>0:
        client_data+=bytes.decode()
        bytes=sock.recv(2048)

    # parse and process the data from the client
    list_of_parts=client_data.split(' ')
    # "12 6"  ["12", "6"]
    # "12  6" ["12", "", "6"]
    # "twelve six" ["twelve", "six"]

    first_string = list_of_parts[0]
    message = ""

    if first_string.find("E") == True:
        x_value = first_string.replace("E", "")
        del list_of_parts[0]
        poly = list_of_parts
        print list_of_parts
        message = "E" + evaluate(x_value, poly)

    elif first_string.find("S") == True:
        a = first_string.replace("S", "")
        del list_of_parts[0]
        b = list_of_parts[0]
        del list_of_parts[0]
        tol = list_of_parts[len(list_of_parts)]
        del list_of_parts[len(list_of_parts)]
        poly = list_of_parts
        message ="S" + bisection(a, b, poly, tol)

    else:
        if first_string.find("E") == False and first_string.find("S") == False:
            message = "Xincorrect calling Character"
        elif first_string.find("S") == True and first_string.replace("S", "") == 0:
            message = "Xx cannot equal zero"
        elif first_string.find("E") == True and first_string.replace("E", "") == 0:
            message = "Xx cannot equal zero"


#write()

    response_bytes=message.encode()
    sock.sendall(response_bytes)
    sock.shutdown(1)  #signal close of the writing the socket




#close()

sock.close()
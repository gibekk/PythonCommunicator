import socket
import sys
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = ('127.0.0.1', 443)
print >>sys.stderr, "starting up on %s port %s" % server
serverSocket.bind(server)
serverSocket.listen(1)

while True:
    print >>sys.stderr, "waiting for a connection"
    connection, client_adress = serverSocket.accept()
    try:
        print >>sys.stderr, 'connection from', client_adress
        while True:
            data = connection.recv(1024)
            print >>sys.stderr, "received '%s'" % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_adress
                break

    finally:
        connection.close()

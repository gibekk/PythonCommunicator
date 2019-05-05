import socket
import sys

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = ('127.0.0.1', 443)
print >>sys.stderr, "connecting to '%s' port '%s'" % server
clientSocket.connect(server)
try:
    message = 'This is the message'
    print >>sys.stderr, "sending '%s'" % message
    clientSocket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = clientSocket.recv(16)
        amount_received += len(data)
        print >>sys.stderr, "received '%s'" % data

finally:
    print >>sys.stderr, 'closing socket'
    clientSocket.close()

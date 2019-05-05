import socket
localSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = ('127.0.0.1', 8888)
print "starting up on %s port %s" % server

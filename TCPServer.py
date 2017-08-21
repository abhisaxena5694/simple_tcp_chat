from socket import *

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()
print 'The server is ready to receive'

while 1:
	
	rcvMsg = connectionSocket.recv(1024)
	if rcvMsg == '*quit*':
		print "Exiting."
		connectionSocket.close()
		exit()
	print rcvMsg
	sendMsg = raw_input('>')
	connectionSocket.send(sendMsg)
	

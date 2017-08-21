from socket import *

# specify serverName and serverPort
serverName = 'localhost'
serverPort = 12000

# Get a TCP socket and connect to the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sendMsg = raw_input('>')
    # if sentence is quit, then send a *quit* message to the server and exit the client app.
    if sendMsg == 'quit':
        clientSocket.send(sendMsg)
        clientSocket.close()
        print "Exiting."
        exit()
    clientSocket.send(sendMsg)
    recvMsg = clientSocket.recv(1024)
    print recvMsg



#modifiedSentence = clientSocket.recv(1024)

#print 'From Server:', modifiedSentence

#clientSocket.close()

"""
This program simulates a TCP client and we will try to connect to a TCP server "
"""
import socket # you imported the socket library, so now you can use all methods and functions inside it
host="127.0.0.1"# Here you enter the IP of the server , if you run the server and the client in the same labtop then use the private ip "127.0.0.1"
port = 12345# the port number of
socket_1= socket.socket()# You created an object called socket_1  or in another words , you created a socket
print "Socket successfully created"
socket_1.connect((host, port)) #connect to the server
message=raw_input(">>") #this line let the user enter a massege
while message != "exit+": #while loop , it will end when the user type "exit+"
   socket_1.send(message)# we send the massege
   data=socket_1.recv(1024) # we will recive a massage with max buffer we set
   print 'Recived massage  ' +str(data) #print the massege we recived from the server
   message=raw_input(">>")#let the user enter a massage again
socket_1.close()# close connection

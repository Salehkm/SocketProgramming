
"""
This program simulates a UDP client and we will try to connect to a UDP server "
"""

import socket# you imported the socket library, so now you can use all methods and functions inside it
host="127.0.0.1"# Here you enter the IP of the server , if you run the server and the client in the same labtop then use the private ip "127.0.0.1"
port = 12355#here you will port number for the client
socket_1= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print "Socket successfully created"
socket_1.bind((host,port))#bind the socket to the ip and port number
server=(host, 12345)#server ip and port number
message=raw_input(">>") #this line let the user enter a massege
while message != "exit+":#while loop , it will end when the user type "exit+"
   socket_1.sendto(message,server)# we send the massege
   data ,addr=socket_1.recvfrom(1024) # we will recive a massage with max buffer we set
   print 'Recived massage  ' + data #print the massege we recived from the server
   message=raw_input(">>")#let the user enter a massage again
socket_1.close()

"""
This program simulates a UDP server, and we will try to connect to it by another program "UDPClient"
"""


import socket # you imported the socket library, so now you can use all methods and functions inside it
host=""# Here you enter the IP of the server , if the client program is run in the same labtop then leave it empty between the two quotation marks
port = 12345
socket_1= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
"""
You created an object called socket_1  or in another words , you created a socket
socket.AF_INET refers to the type of address and protocol
socket.SOCK_DGRAM is the type of the socket
"""
print "Socket successfully created"
socket_1.bind((host, port))# this line let you bind the server to the chosen IP and port number
print "socket binded to %s" %(port)
print "Server Started"
while True:#this loop is an infinte loop , means it will not end until you close the program
   data, addr = socket_1.recvfrom(1024)
   """
   since it is a UDP server it may connect to more than 1 client
   so every time we recive a massege , we will print the address of the massege source
   """
   print 'massege from: '+str(addr)#print the source address
   print 'massege: '+str(data)#print the recived massege
   socket_1.sendto(data,addr)#reply to the source , if want reply with another massege change data to the massege you want to send like: socket_1.sendto("Welcome",addr)
socket_1.close() #close the connection ,or shut down the server

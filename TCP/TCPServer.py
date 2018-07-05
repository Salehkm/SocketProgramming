"""
This program simulates a TCP server, and we will try to connect to it by another program "TCPClient"
"""

import socket # you imported the socket library, so now you can use all methods and functions inside it
host="" # Here you enter the IP of the server , if the client program is run in the same labtop then leave it empty between the two quotation marks
port = 12345 # Here you choose the port number of the server which you want to listen to
socket_1= socket.socket() # You created an object called socket_1  or in another words , you created a socket
print "Socket successfully created"
socket_1.bind((host, port)) # this line let you bind the server to the chosen IP and port number
print "socket binded to %s" %(port)
socket_1.listen(1) # listen command let you listen to the socket you created, waiting for connection from the client . you can set the number of clients you want to listen to in the same time
print "socket is listening"
conn, addr = socket_1.accept()
"""
 There are 2 variables , conn and addr .
 accept() means the server accepted the connection from the client
 accept() method returns two values;data and the address of the client
so we let the variable conn equal to the connection and addr equal to the address of the client
"""
print 'Got connection from', addr
while True:#this loop is an infinte loop , means it will not end until the break condition is true
   data=conn.recv(1024) # data varible is equal to the conn , we will recive a massage with max buffer we set
   print 'massege: '+str(data)# data varible is not string , so str command convert it to sting variable
   if not data :#our break condition , means when there is no data will break the loop
     break
   conn.send(data)# part of the loop , which send data varible to the client *** note that you can change the massege you sent , like : conn.send("Welcome")
conn.close()# you need close the connection in the end of the program

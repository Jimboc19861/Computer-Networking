#Computer Networking Coursework
#
#This programme is the server side. The server creates a socket constantly awaits messages from the client.
#
#The server receives 3 distinct UDP packets from the client and concatenates them together using two '#' as separators.
#
#It computes the total length of the packets and returns the concatenated word and length back to the client as 2
#distinct packets n and R.
#
#James Cordery - 13184228
#2nd April 2020

import socket
import socketserver
import time

serverSocket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #This creates the server socket.

UDP_IP = "localhost"
UDP_PORT = 6842
address = ("localhost" , 6842)

serverSocket.bind(address) # The server binds to the socket and awaits messages from the client. 
print ("Waiting for client...")

while True:
    message1,address = serverSocket.recvfrom(1024) #A while loop is created to await the messages and print them
    print ("Received: ",message1," from",address)  #along with their length. Once complete, the while loop ends.
    print ("Message length: " , (len(message1)))
    message2,address = serverSocket.recvfrom(1024)
    print ("Received: ",message2," from",address)
    print ("Message length: " , (len(message2)))
    message3,address = serverSocket.recvfrom(1024)
    print ("Received: ",message3," from",address)
    print ("Message length: " , (len(message3)))
    break

packet1 = message1.decode(encoding = 'utf-8' , errors = 'strict') # The server decodes the messages ready to join
packet2 = message2.decode(encoding = 'utf-8' , errors = 'strict') # them.
packet3 = message3.decode(encoding = 'utf-8' , errors = 'strict') 

print("*" * 50)

length =(len(packet1) + len(packet2) + len(packet3)) # The server adds the message lengths together and prints the 
print("Total Package Length: " , length)             #result.
joined = packet1 + "#" + packet2 + "#" + packet3 # The server concatenates the 3 packets and adds in two '#'
print("Concatenated Packets: " , joined)         #separators and prints the result.

print("*" * 50)

R = str.encode(joined)           #The server encodes the concatenated packets and total length and sends them back to 
serverSocket.sendto(R , address) #the client as 2 distinct UDP packets n and R.
n = repr(length).encode('utf-8')
serverSocket.sendto(n , address) 

print ("Sent 3 packets to client" , "\n") # Lets the client know the packets have been sent and goes back to waiting.
print ("Waiting for client...")
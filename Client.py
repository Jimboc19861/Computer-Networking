#Computer Networking Coursework
#
#This programme creates a socket and prompts the user to enter 3 distinct packets.
#The packets are then sent to a created server where they will be concatenated together along with two '#' as separators
#
#The client then awaits two return messages from the server, n and R. It then removes the '#' separators 
#and checks the complete message is the same as the concatenated entries from the user as well as the length and 
#prints the results.
#
#James Cordery - 13184228
#2nd April 2020

import socket
import socketserver
import time

clientSock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #This creates the client socket

UDP_IP = "localhost" 
UDP_PORT = 6842 
address = ("localhost" , 6842)

s1 = str(input("Please enter Packet number 1: ")) #The user is prompted for 3 inputs which are then incoded as bytes
message1 = str.encode(s1)                         #and sent to the client
clientSock.sendto(message1 , address)
s2 = str(input("Please enter Packet number 2: "))
message2 = str.encode(s2)
clientSock.sendto(message2 , address)
s3 = str(input("please enter Packet number 3: ")) 
message3 = str.encode(s3)
clientSock.sendto(message3 , address)

l = (len(s1) + len(s2) + len(s3)) #The messages are added together and printed.
print("Total message length: " , l)
C = s1 + s2 + s3 #The message lengths are added together and printed. 
print ("Complete message: " , C)

print ("Sent 3 packets to server") #A message is printed to let the client know the packets have been sent.
print ("Waiting to receive message...") #The client then awaits a retrun message from the server.
print ("*" * 50) 

R, address = clientSock.recvfrom(1024) #The client receives a string R from the server.
print("Message received: " , R)
R = R.decode(encoding = "utf-8" , errors = "strict")
R = (R.replace('#' , '')) #The client removes the '#' separators and prints the result.
if R == C: #Here it checks that the received message matches the complete message the client originally sent. 
    print("Concatenation Correct") #It prints a message of they match or an error if they are different. 
else:
    print("Error, messages do not match!")

n, address = clientSock.recvfrom(1024) #The client receives an integer n from the server.
print("Message Received: " , n)
N = n.decode(encoding = "utf-8" , errors = "strict")
n = int(N) #The client decodes the message and converts it back to an integer.
if n == l: #Here the client runs an if statement to check that the length matches the original combined length of packets.
    print("Length Correct")
else:
    print("Error, message length does not match!")

print("Decoded Message: " , R)
print("Decoded Message Length: " , n)

clientSock.close() #Once complete, the client closes the socket connection.
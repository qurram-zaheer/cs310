#!/usr/bin/python           
import random
import socket               # Import socket module
import pickle
import random 

s = socket.socket()         # Create a socket object
host = socket.gethostbyname('localhost') # Get local machine name/for this example
ports = 12345             #server port
portc = 32451 	   #client's own port for incoming connections (if any)
s.bind((host, portc))
s.connect((host, ports))
print ("\n\n",s.recv(1024))
x=input()
xp=pickle.dumps(x)
s.send(xp)


  
# using list comprehension + randrange()  
# to generate random number list 
len=random.randrange(25,100)
res = [random.randrange(1, 100, 1) for i in range(len)] 
print("\n\nPre Sorting List")
print(res)
data=pickle.dumps(res)
res.sort()
print("\n\nSorted List")
print(res)

s.send(data)
if(x==1):
    val=s.recv(1024)
    flist=pickle.loads(val)
    print("\n\nFinal List:")
    print(flist)

rp=s.recv(1024)
repeated=pickle.loads(rp)
print("\n\nRepeated values")
repeated.sort()
print(repeated)
#str1="thank you for the service"
#msg=str1.encode
s.send(b"Thank you for speaking")
s.close                     # Close the socket when done

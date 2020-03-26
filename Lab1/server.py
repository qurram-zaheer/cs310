import socket
from ast import literal_eval

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname('localhost') # Get local machine name
port = 12345 
ports = 32451               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print ('host ip', host)
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(b'Thank you for connecting')
   print(c.recv(1024))
   b = c.recv(1024).decode('utf-8')
   out = literal_eval(b)
   seen = {}
   duplicates = []
   for x in out:
      if x not in seen:
         seen[x]=1
      else:
         if seen[x]==1:
            duplicates.append(x)
         seen[x]+=1
   
   
   #out = list(dict.fromkeys(out))
   temp = list(dict.fromkeys(out)) 
   c.send(bytes(str(temp),'UTF-8'))
   c.send(bytes(str(seen),'UTF-8'))
   c.close()                # Close the connection
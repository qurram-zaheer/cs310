import socket
from ast import literal_eval
import random

  
N = 10
rando = []
for i in range(N):
  rando.append(random.randint(1,5))

s = socket.socket()
host = socket.gethostbyname('localhost')
portc = 32451
ports = 12345

s.bind(('0.0.0.0',portc))

s.connect(('10.59.122.36',ports)) #connection between lab system 11 (client) and 9 (server)

s.send(b'It was nice talking to you, other computer')
print(s.recv(1024))
s.send(bytes(str(rando).encode('UTF-8')))
temp = s.recv(N*1024).decode('utf-8')
output = literal_eval(temp)
print(output)

s.close()



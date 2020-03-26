import socket
import random
from ast import literal_eval

clientArray = []
N = 10
for i in range(N):
  clientArray.append(random.randint(1,10))
s = socket.socket()

host = socket.gethostbyname('localhost')
ports = 12345
portc = 32451

s.bind((host,portc))

s.connect((host,ports))
print(s.recv(1024))
s.send(b'It was nice talking to you')
print('Created Array: ',clientArray)
s.send(bytes(str(len(clientArray)).encode('utf-8')))
s.send(bytes(str(clientArray).encode('utf-8')))
print(s.recv(1024))
clientChoice = input()
s.send(bytes(str(clientChoice).encode('utf-8')))
serverOutput = s.recv(N*1024).decode('utf-8')
serverOutput = literal_eval(serverOutput)
print(serverOutput)



import socket
import random
from ast import literal_eval

N = random.randint(25,100)
rando = []
for i in range(N):
    rando.append(random.randint(1,100))


s = socket.socket()
host = socket.gethostbyname('localhost')
portc = 5000
ports = 12345

s.bind((host,portc))

s.connect((host,ports))
print (s.recv(1024))
s.send(b'It was nice talking to you')
print('\nCreated array: ',rando)
s.send(bytes(str(rando).encode('UTF-8')))
temp = s.recv(N*1024).decode('utf-8')
out = literal_eval(temp)
print('\nFiltered array: ',out)
temp2 = s.recv(N*1024).decode('utf-8')
duplicates = literal_eval(temp2)
print('Duplicates: ',duplicates)
print('hello')
s.close()
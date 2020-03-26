import socket
import random
from ast import literal_eval

def mergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:] 
  
        mergeSort(left) 
        mergeSort(right) 
  
        i = j = k = 0
          
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
          
        
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1

def intersection(list1, list2):
  listOut = [value for value in list1 if value in list2]
  listOut = list(dict.fromkeys(listOut))
  mergeSort(listOut)
  return listOut

N = 10
randoS = []
for i in range(N):
  randoS.append(random.randint(1,5))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

host = socket.gethostbyname('localhost')
portc = 32451
ports = 12345

s.bind(('0.0.0.0',ports))
print('host ip',host)
s.listen(5)
while True:
  c,addr = s.accept()
  print ('Got connection from', addr)
  c.send(b'Thank you for connecting')
  print(c.recv(1024))
  inputArr = c.recv(N*1024).decode('utf-8')
  inputArr1 = literal_eval(inputArr)
  print('Array received: ',inputArr1)
  print('Array created by server: ',randoS)
  output = intersection(inputArr1,randoS)
  # output.sort()
  print(output)
  c.send(bytes(str(output),'UTF-8'))
  c.close()
  

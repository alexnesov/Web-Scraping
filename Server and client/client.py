import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((os.environ.get('IP_MYDEVICE'),1234)) 

msg = s.recv(1024)
print(msg.decode("utf-8"))

# Type "ipconfig" in command prompt on Windows to get your IPV4
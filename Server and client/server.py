import socket
import os

test="hello world"

def set_server_connection(test):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((os.environ.get('IP_MYDEVICE'),1234)) #Windows IP Address
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f'Connection from {address} has been established!')
        test = str(test)
        clientsocket.send(bytes(test, "utf-8"))
        clientsocket.close()
        break

    s.close()



# http://code.activestate.com/recipes/578802-send-messages-between-computers/
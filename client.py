from socket import *
import os,sys
from threading import Thread

PORT=8888
HOST='127.0.0.1'
ADDR=(HOST,PORT)

def send_msg(s,name):
    while True:
        text=input('发言：')
        msg='C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr=s.recvfrom(2048)
        print(data.encode())


def main():
    a=[]
    q=[]
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input('请输入姓名:')
        msg='L '+name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(1024)
        if data.decode()=='OK':
            print('您已进入聊天室!')
            break
        else:
            print(data.decode())

    pid=os.fork()
    if pid<0:
        sys.exit("Error!")
    elif pid==0:
        send_msg(s)
    else:
        recv_msg(s)


if __name__ == '__main__':
    main()

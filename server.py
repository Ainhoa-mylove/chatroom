"""
chat room
env:python 3.5
socket fork practise
"""
from socket import *
import os,sys
from threading import Thread

PORT=8888
HOST='127.0.0.1'
ADDR=(HOST,PORT)
user={}

def do_login(s,name,addr):
    if name in user:
        s.sendto('该用户已存在！'.encode(),addr)
        return
    s.sendto(b'OK',addr)
    msg='欢迎%s进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])

    user[name]=addr

def do_chat(s,name,text):
    if text=='quit':
        sys.exit('退出服务!')
    else:
        msg='%s : %s'%(name,text)
        for i in user:
            if i!=name:
                s.sendto(msg.encode(),user[i])

def do_request(s):
    print('Listen the port 8888')
    while True:
        data,addr=s.recvfrom(1024)
        msg=data.decode().split(' ')
        if msg[0]=='L':
            do_login(s,msg[1],addr)
        elif msg[0]=='C':
            text=' '.join(msg[2:])
            do_chat(s,msg[1],text)

def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    do_request(s)

if __name__ == '__main__':
    main()

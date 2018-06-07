# coding:utf8  
  
'''''创建服务器端程序，用来接收客户端传进的文件'''  

from socket import *              #引入socket模块内的函数，创建一个套接口
import thread              #引入thread模块内的函数

def tcplink(skt,addr):            
    print(skt)
    print("Connect by...",addr)         #显示连接状态
    print('Start receiving file')      #开始传输数据
    with open('./ww.jpg', 'rb') as f:    #以二进制读的方式打开文件
        for data in f:       
            print(data)            #输出文件中的数据
            skt.send(data)          #发送TCP数据，将字符型数据发送到连接的客户端
    f.close()           #关闭文件
    skt.close()


HOST = "127.0.0.1"               #指定ip为本机ip地址
PORT = 50000                     #指定监听端口为50000
ADDR = (HOST,PORT)               #指定地址，以元组（host,port）的形式表示地址

server = socket(AF_INET,SOCK_STREAM)          #建立服务器之间的网络通信，建立基于TCP的流式套接口（SOCK_STREAM 类型是基于TCP的，有保障的面向连接的socket）
server.bind(ADDR)             #调用服务端的bind(address)函数，将套接字绑定到指定地址
server.listen(5)           #调用服务器端listen(backlog)监听函数开始监听TCP传入连接，backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量，该值至少为1，大部分应用程序设为5即可

while True:
    print("Waiting for connect..")     #显示等待连接提示
    skt,addr = server.accept()           #调用服务器端accept()函数，接受client端TCP连接
    print(skt)
    try:                                                #异常处理，把可能发生错误的语句放在try模块里，用except来处理异常
        thread.start_new_thread(tcplink,(skt,addr))
    except:
        print("Cannot begin")
server.close()              #关闭套接字

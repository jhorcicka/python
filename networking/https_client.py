#!/usr/bin/python

import socket, ssl

HOST = "www.youtube.com"
PORT = 443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock = context.wrap_socket(s, server_hostname=HOST)
s_sock.connect((HOST, PORT))
#s_sock.send("GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n ".encode())
s_sock.send("GET / HTTP/1.1\r\n\r\n ".encode())

while True:
    data = s_sock.recv(2048)
    if ( len(data) < 1 ) :
        break
    print(data)

s_sock.close()

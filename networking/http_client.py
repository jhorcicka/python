#!/usr/bin/python

import socket

class HttpClient: 
  def __init__(self):
    self.__host = '127.0.0.1'
    self.__port = 8080 

  def run(self):
    s = socket.socket()
    s.connect((self.__host, self.__port))
    #request = "GET /manager/html HTTP/1.1\r\n\r\n"
    #request = "GET /manager/html HTTP/1.1\n\n"
    request = " GET /tmp/index.html\r\n\r\n"
    s.send(request.encode())
    response = s.recv(2048)
    print(response)
    #print(response.decode())
    s.close()

if __name__ == '__main__':
  client = HttpClient()
  client.run()

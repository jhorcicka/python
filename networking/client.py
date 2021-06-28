#!/usr/bin/python

import socket

class Client: 
  def __init__(self):
    self.__socket = None
    self.__host = '127.0.0.1'
    self.__port = 12345

  def run(self):
    self.__socket = socket.socket()
    self.__socket.connect((self.__host, self.__port))
    response = self.__socket.recv(1024)
    print(response.decode())
    self.__socket.close()

if __name__ == '__main__':
  client = Client()
  client.run()

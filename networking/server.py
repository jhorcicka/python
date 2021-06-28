#!/usr/bin/python

import socket

class Server: 
  def __init__(self):
    self.__socket = socket.socket()
    self.__port = 12345
    self.__socket.bind(('', self.__port))
    self.__socket.listen(5)
    self.__counter = 0

  def start(self):
    while True:
      c, addr = self.__socket.accept()
      self.__counter += 1
      response = str.encode('Response ' + str(self.__counter))
      c.send(response)
      c.close()

if __name__ == '__main__':
  server = Server()
  server.start()

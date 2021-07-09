#!/usr/bin/python

class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

# decorators

def print_it(fce):
  def inner(*args):
    x = fce(args[0])
    print(x)
  return inner

@print_it
def say_hi(name):
  return "Hello, " + str(name)


if __name__ == "__main__":
  say_hi("Tom")

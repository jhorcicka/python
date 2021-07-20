#!/usr/bin/python

class X:
  def __init__(self):
    self._x = 0

  def get_x(self):
    return self._x

  def set_x(self, x):
    self._x = x

  def del_x(self):
    del self._x

  x = property(get_x, set_x, del_x, "doc_x")

class Y:
  def __init__(self):
    self._y = 0

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self._y = y


x = X()
print(x.x)
x.x = 50
print(x.x)


y = Y()
print(y.y)
y.y = 100
print(y.y)


#!/usr/bin/python

class QuickSorter:
  def __init__(self, data):
    self._data = data
    self._pivot = -1

  def get_data(self):
    return self._data

  def sort(self):
    self._quicksort(0, len(self._data) - 1)

  def _partition(self, left_start, right_start, left_index, right_index):
    while self._data[left_index] < self._pivot and left_index < right_start:
      left_index += 1
    while self._data[right_index] > self._pivot and right_index > left_start:
      right_index -= 1

    if left_index <= right_index:
      tmp = self._data[left_index]
      self._data[left_index] = self._data[right_index]
      left_index += 1
      self._data[right_index] = tmp
      right_index -= 1

    return (left_index, right_index)

  def _quicksort(self, left_start, right_start):
    left_start = left_start
    right_start = right_start
    self._pivot = self._data[int((left_start + right_start) / 2)]
    left_index = left_start
    right_index = right_start

    (left_index, right_index) = self._partition(left_start, right_start, left_index, right_index)
    while left_index < right_index:
      (left_index, right_index) = self._partition(left_start, right_start, left_index, right_index)

    if right_index > left_start: 
      self._quicksort(left_start, right_index)
    if left_index < right_start: 
      self._quicksort(left_index, right_start)


if __name__ == '__main__':
  data = [2, 8, -1, 5, 7, -4, 9, 3, 6]
  sorter = QuickSorter(data)
  print(sorter.get_data())
  sorter.sort()
  print(sorter.get_data())

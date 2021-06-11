#!/usr/bin/python

import random
import math
import sys

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, point):
    if point == None:
      return sys.maxsize
    return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

  def __str__(self):
    return "P[%s, %s]" % (self.x, self.y)

class KMeans:
  OUTPUT_FILE = 'data.csv'
  POINTS_COUNT = 10
  CLUSTERS_COUNT = 2

  def __init__(self):
    self._points = []
    self._clusters = {}
    self._clusters_changed = True

  def run(self):
    self.generate_points()
    self.write_points()
    self.initialize_clusters()
    while self._clusters_changed:
      old_hash = self.clusters_hash()
      self.compute_new_centroids()
      self.sort_points()
      new_hash = self.clusters_hash()
      self._clusters_changed = not (old_hash == new_hash)
      self.debug()

  def generate_points(self):
    for i in range(0, self.POINTS_COUNT):
      x = self.get_random_int()
      y = self.get_random_int()
      self._points.append(Point(x, y))

  def write_points(self):
    with open(self.OUTPUT_FILE, 'w') as output_file:
      output_file.write("x\ty\n")
      for point in self._points:
        output_file.write("%s\t%s\n" % (point.x, point.y))

  def get_random_int(self):
    return random.randint(0, 30)

  def initialize_clusters(self):
    for i in range(0, self.CLUSTERS_COUNT):
      self._clusters[self._points[i]] = []

  def sort_points(self):
    for point in self._points:
      centroid = self.find_closest_centroid(point)
      self.add_point(centroid, point)

  def compute_new_centroids(self):
    new_clusters = {}
    for old_centroid in self._clusters.keys(): 
      points = self._clusters[old_centroid]
      if len(points) == 0:
        points = [old_centroid]
      new_centroid = self.get_average_point(points)
      new_clusters[new_centroid] = []
    self._clusters = new_clusters

  def get_average_point(self, points):
    x_sum = 0
    y_sum = 0
    for point in points:
      x_sum += point.x
      y_sum += point.y
    count = len(points)
    x = int(x_sum / count)
    y = int(y_sum / count)
    return Point(x, y)

  def add_point(self, centroid, point):
    if not centroid in self._clusters:
      self._clusters[centroid] = [point]
    else:
      self._clusters[centroid].append(point)

  def find_closest_centroid(self, point):
    min_distance = sys.maxsize
    final_centroid = None
    for centroid in self._clusters.keys(): 
      distance = point.distance(centroid)
      if distance < min_distance:
        min_distance = distance
        final_centroid = centroid
    return final_centroid

  def debug(self):
    print("DEBUG\n=====")
    text = ''
    for centroid in self._clusters.keys():
      text += str(centroid) + ": "
      for point in self._clusters[centroid]:
        text += str(point) + ", "
      text += "\n"
    print(text)

  def clusters_hash(self):
    hash = ''
    for centroid in self._clusters.keys():
      hash += str(centroid) + ":" + str(len(self._clusters[centroid])) + "; "
    return hash
      

if __name__ == '__main__':
  k_means = KMeans()
  k_means.run() 


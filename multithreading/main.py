#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import logging
import threading
import time

TASK_TIME = 2
THREADS_COUNT = 5
LOGGING_FORMAT = "%(asctime)s: %(message)s"
TIME_FORMAT = "%H:%M:%S"

def threadTask(name):
  logging.info("Thread %s: starting", name)
  time.sleep(TASK_TIME)
  logging.info("Thread %s: finishing", name)

def createThreads(count):
  threads = []
  for i in range(0, count):
    threads.append(threading.Thread(target=threadTask, args=(i,)))
  return threads

if __name__ == "__main__":
  logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO, datefmt=TIME_FORMAT)
  logging.info("Before creating threads")
  threads = createThreads(THREADS_COUNT)
  logging.info("Before running threads")
  for t in threads:
    t.start()
  logging.info("Wait for threads to finish")
  for t in threads:
    t.join()
  logging.info("All done")


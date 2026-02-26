import math
import random

random.seed(42)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

data = [
  [11, 1, 1],
  [3, 35, 0],
  [10, 0, 1],
  [0, 10, 0],
  [21, 1, 1],
  [4, 15, 0],
  [10, 2, 1],
  [1, 15, 0],
  [7, 3, 1],
  [2, 12, 0],
  [20, 2, 1],
  [2, 21, 0]
]

w_letters = random.uniform(-1, 1)
w_numbers = random.uniform(-1, 1)
bias = random.uniform(-1, 1)

learning_rate = 0.01
epochs = 50000

for epoch in range(epochs):
  for count_letters, count_numbers, label in data:
    z = w_letters * count_letters + w_numbers * count_numbers + bias
    output = sigmoid(z)

error = label - output

w_letters += learning_rate * error * count_letters
w_numbers += learning_rate * error * count_numbers
bias += learning_rate * error

test_files = [
  [10, 1],
  [10, 0],
  [15, 2],
  [9, 2], 
  [1, 10],
  [3, 15],
  [0, 10] 
]

for count_letters, count_numbers in test_files:
  z = w_letters * count_letters + w_numbers * count_numbers + bias
  output = sigmoid(z)
  prediction = "Letter" if output > 0.5 else "Number"
  print(f"Letters: {count_letters}, Numbers: {count_numbers} => {prediction}")

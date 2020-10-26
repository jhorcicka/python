#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The description says. 
# There must be a random answer and the player has 10 chances to guess the random number between 1-100.
# When it's higher it has to say something like not correct it has to be higher! And lower visa versa. 
# If correct it has to say it as well. Otherwise after 10 tries it has to say you failed. 
# And if you guess the right one it also has to say in how many rounds.
#

import random
import math

MAX_ROUNDS = 10
MAXIMUM_NUMBER = 100

def start():
  answer = random.randint(1, MAXIMUM_NUMBER)
  finished = False
  rounds = 0

  while not finished:
    rounds += 1
    user_number = int(input("Guess a number between 1 and %d:" % (MAXIMUM_NUMBER)))

    if user_number == answer: 
      print("You got the right answer in %d rounds!" % (rounds))
      finished = True
    elif user_number <= answer:
      print("That is not correct, it has to be higher!")
    elif user_number >= answer:
      print ("That is not correct, it has to be lower!")
          
    if rounds > MAX_ROUNDS:
      print("You have failed to guess the number in %d rounds!" % (max_turns))
      finished = True


if __name__ == '__main__':
  start()

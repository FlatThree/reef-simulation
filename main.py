# TO FIX: ANIMALS CAN MOVE MORE THAN ONCE IF THEY MOVE DOWN OR RIGHT

import numpy
from numpy import random

class Animal:
  def __init__(self, name):
    self.name = name

class Shark(Animal):
  pass

class Fish(Animal):
  pass

class Algae:
  pass

class Reef:

  # initialize a square array with random numbers 0 to 3
  def __init__(self, length):
    # length = side length of the array
    self.length = length
    self.array = random.randint(4, size=(length, length))

  # update the reef
  def update(self):
    # go through all the indexes of the array line by line
    for (x, y), cell in numpy.ndenumerate(self.array):
      if cell != 0 and cell != 1:
        self._update_cell(x, y, cell)
  
  # update a single cell that isn't empty or algae
  def _update_cell(self, x, y, cell):
    # choose a random direction to move in
    direction = random.randint(0, 4)

    if direction == 0:
      return
    elif direction == 1:
      new_x = x
      new_y = y + 1
    elif direction == 2:
      new_x = x + 1
      new_y = y
    elif direction == 3:
      new_x = x
      new_y = y - 1
    else:
      new_x = x - 1
      new_y = y
    
    # make sure new cell isn't outside the array
    if (new_x >= 0 and new_y >= 0) and (new_x < self.length and new_y < self.length):
      # move if new cell is empty
      if self.array[new_x, new_y] == 0:
        self._move(x, y, new_x, new_y)
      # reproduce if new cell has same animal
      elif self.array[new_x, new_y] == self.array[x, y]:
        self._reproduce(x, y, new_x, new_y)
      # if all else fails, eating is always the correct answer
      else:
        self._eat(x, y, new_x, new_y)

  def _move(self, x, y, new_x, new_y):
    self.array[new_x, new_y] = self.array[x, y]
    self.array[x, y] = 0
  
  def _reproduce(self, x, y, new_x, new_y):
    pass
  
  def _eat(self, x, y, new_x, new_y):
    if self.array[new_x, new_y] == self.array[x, y] - 1:
      self._move(x, y, new_x, new_y)

if __name__ == "__main__":
  reef = Reef(10)
  for i in range(10):
    print("Day", i)
    print(reef.array)
    reef.update()
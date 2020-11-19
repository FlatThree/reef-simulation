import numpy
from numpy import random

class Animal:
  def __init__(self, name):
    self.name = name

class Predator(Animal):
  def __init__(self, name):
    self.name = name

class Prey(Animal):
  def __init__(self, name):
    self.name = name

class Plant:
  def __init__(self, name):
    self.name = name

class Reef:
  def __init__(self, length):
    # create a square array with side length and numbers 0 to 3
    self.length = length
    self.array = numpy.random.randint(4, size=(length, length))
  
  def update(self):
    # go through all the indexes of the array
    for (x, y), cell in numpy.ndenumerate(self.contents):
      if cell != 0:
        self._update_cell(x, y, cell)

  def _update_cell(self, x, y, cell):
    direction = random.randint(0, 4)

    if direction == 0:
      return
    elif move == 1:
      # go up
    elif move == 2:
      # go right
    elif move == 3:
      # go down
    else:
      # go left
    
    if self.contents[new_x, new_y] == 0:
      self._move(x, y, new_x, new_y)
    else:
      # _reproduce
      # _eat

  def _move(self, x, y, new_x, new_y):
    self.contents[new_x, new_y] = self.contents[x, y]
    self.contents[x, y] = 0

  def _eat(self)
  def _reproduce(self)



r = Reef(10)
x = 1
for (index,ina), a in numpy.ndenumerate(r.array):
  print(index)
import numpy as np
import random

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
  def __init__(self, size):
    self.size = size
    self.contents = np.array()
    for i in range(self.size):
      pass
  
  @property
  def size(self):
    return self.size
  
  def update(self):
    for (x, y), cell in np.ndenumerate(self.contents):
      if cell is not None:
        self._update_cell(x, y, cell)
  
  def _update_cell(self):
    move = random.randint(0, 9)
    
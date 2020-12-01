# TO DO: reproduction
# TO FIX: ANIMALS CAN MOVE MORE THAN ONCE IF THEY MOVE DOWN OR RIGHT

import numpy as np
from numpy import random

import matplotlib
import matplotlib.pyplot as plt

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
    self.array = random.choice([0, 1, 2, 3], p=[0.25, 0.35, 0.3, 0.1], size=(length, length)) # ratios based off of https://science.sciencemag.org/content/349/6252/aac6284
    self.shark_data = []
    self.fish_data = []
    self.algae_data = []

  # update the reef
  def update(self):
    # go through all the indexes of the array line by line
    for (x, y), cell in np.ndenumerate(self.array):
      if cell != 0 and cell != 1:
        self._update_cell(x, y, cell)
    
    self.shark_data.append(np.count_nonzero(self.array == 3))
    self.fish_data.append(np.count_nonzero(self.array == 2))
    self.algae_data.append(np.count_nonzero(self.array == 1))
    print("Sharks: " + str(self.shark_data))
    print("Fish: " + str(self.fish_data))
    print("Algae: " + str(self.algae_data))
  
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
    if np.any(self.array):
      print("reproduce")
  
  def _eat(self, x, y, new_x, new_y):
    if self.array[new_x, new_y] == self.array[x, y] - 1:
      self._move(x, y, new_x, new_y)

if __name__ == "__main__":
  reef = Reef(10)
  for i in range(10):
    print("Day", i)
    print(reef.array)
    reef.update()

plt.plot(reef.shark_data)
plt.plot(reef.fish_data)
plt.plot(reef.algae_data)
plt.show()
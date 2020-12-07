# TO FIX: ANIMALS CAN MOVE MORE THAN ONCE IF THEY MOVE DOWN OR RIGHT

import numpy as np
from numpy import random

import matplotlib.pyplot as plt

class Reef:

  # initialize a square array with random numbers 0 to 3
  def __init__(self, length):
    # length = side length of the array
    self.length = length
    self.array = random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1], size=(length, length))
    self.shark_data = []
    self.fish_data = []
    self.algae_data = []

  # update the reef
  def update(self):
    print("Updating...")
    # go through all the indexes of the array line by line
    for (x, y), cell in np.ndenumerate(self.array):
      if cell != 0 and cell != 1:
        self._update_cell(x, y, cell)
    
    # count at the end of each day
    self.shark_data.append(np.count_nonzero(self.array == 3))
    self.fish_data.append(np.count_nonzero(self.array == 2))
    self.algae_data.append(np.count_nonzero(self.array == 1))
    print("Sharks: " + str(self.shark_data))
    print("Fish: " + str(self.fish_data))
    print("Algae: " + str(self.algae_data))

    self._algae_spawn()
  
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
      # reproduce if new cell has same animal and there are empty cells
      elif self.array[new_x, new_y] == self.array[x, y]:
        self._reproduce(x, y)
      # if all else fails, eating is always the correct answer
      else:
        self._eat(x, y, new_x, new_y)

  def _move(self, x, y, new_x, new_y):
    self.array[new_x, new_y] = self.array[x, y]
    self.array[x, y] = 0
  
  def _reproduce(self, x, y):
    if np.any(self.array == 0):
      x_choices = []
      y_choices = []

      # if there's an empty cell, add it to the list
      for (i,j), cell in np.ndenumerate(self.array):
        if cell == 0:
          x_choices.append(i)
          y_choices.append(j)

      spawn_x = random.choice(x_choices)
      spawn_y = random.choice(y_choices)

      # spawn the animal in a random empty space
      self.array[spawn_x, spawn_y] = self.array[x, y]

      #print("repro at: (" + str(spawn_x) + ", " + str(spawn_y) + ")")
  
  def _eat(self, x, y, new_x, new_y):
    if self.array[new_x, new_y] == self.array[x, y] - 1:
      self._move(x, y, new_x, new_y)
  
  def _algae_spawn(self):
    if np.any(self.array == 0):
      # spawn 1/3 of the current algae
      for i in range(int(self.algae_data[-1]/3)):
        x_choices = []
        y_choices = []

        # if there's an empty cell, add it to the list
        for (i,j), cell in np.ndenumerate(self.array):
          if cell == 0:
            x_choices.append(i)
            y_choices.append(j)

        spawn_x = random.choice(x_choices)
        spawn_y = random.choice(y_choices)

        # spawn the algae in a random empty space
        self.array[spawn_x, spawn_y] = 1
        #print("algae repro at: (" + str(spawn_x) + ", " + str(spawn_y) + ")")

if __name__ == "__main__":
  size = int(input("\nSize of the reef?\nMust be at least 10.\n"))

  if size < 10:
    valid_size = False

    while valid_size is False:
      size = int(input("\nInvalid answer.\nMust be at least 10.\n"))
      if size >= 10:
        valid_size = True
  
  days = int(input("\nHow many days?\nMust be at least 1.\n"))

  if days < 1:
    valid_days = False

    while valid_days is False:
      days = int(input("\nInvalid answer.\nMust be at least 1.\n"))
      if size >= 1:
        valid_days = True

  reef = Reef(size)
  for i in range(days):
    print("Day", i)
    print(reef.array)
    reef.update()

# plotting the data
plt.plot(reef.shark_data, marker="o")
plt.plot(reef.fish_data, marker="o")
plt.plot(reef.algae_data, marker="o")

labels = ["Tiger Sharks", "Clownfish", "Algae"]

plt.legend(labels)
plt.show()
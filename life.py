
'''
import numpy as np
import random
from numpy.random import randn

class Animal:
  def __init__(self, name, food, energy=100, repro=150, fatigue=10):
    self.name = name
    self.kingdom = 'Animal'
    self.energy = energy
    self.food = food
    self.repro = repro
    self.fatigue = fatigue
  
  def act(self, critter, view):
    print(critter)
    
    if len(critter) > 0:

      # check for food around
      grub = {}
      for grubkey in view.neighbors.keys():
        if view.neighbors[grubkey][1] == self.food:
          grub[grubkey] = view.neighbors[grubkey]
      
      print(grub)

      if (len(view.spaces) > 0) & (critter[3] > critter[4]):
        #dirRepro = spaces[random.choice(list(spaces.keys()))]
        dirRepro = random.choice(view.spaces)
        baby = {'location':dirRepro, 'energy':(-1 * critter[3] / 2), 'act':'repro'}
        
        #print(self.name + ' gives birth at ' + str(baby))
        return baby
      
      #EAT, if there's food nearby
      elif len(grub.keys()) > 0:
        # pick a random selection from the food options
        pick = random.choice([x for x in grub.keys()])
                    
        # then eat it
        eat = {'location':pick, 'energy':grub[pick][3] / 2, 'act':'eat'}

        #print(self.name + ' eats ' + grub.loc[pick, 'name'])
        return eat
        
      #MOVE, if there's space
      elif len(view.spaces) > 0:
        dirMove = random.choice(view.spaces)
        move = {'location':dirMove, 'energy':-1 * critter[5], 'act':'move'}
        return move
      else:
        return None
  def birthStats(self):
    # set critter's starting stats
    birthEn = int(self.energy + (np.random.randn(1)[0] * 20))
    birthRe = int(self.repro + (np.random.randn(1)[0] * 10))
    birthFa = int(self.fatigue + (np.random.randn(1)[0] * 5))
    if birthFa < 5:
      birthFa = 5
    
    # save for passing on to offspring
    inheritance = {'birthEn': birthEn, 'birthRe': birthRe, 'birthFa': birthFa}
    return [self.name, self.kingdom, inheritance, birthEn, birthRe, birthFa]

class Predator(Animal):
  def __init__(self, name, food = 'Prey', energy = 200, repro = 310, fatigue = 20):
    Animal.__init__(self, name, food, energy, repro, fatigue)
    self.kingdom = 'Predator'

class Prey(Animal):
  def __init__(self, name, food = 'Plant', energy = 100, repro = 150, fatigue = 10):
    Animal.__init__(self, name, food, energy, repro, fatigue)
    self.kingdom = 'Prey'


#create class Plant
class Plant:
  def __init__(self, name, energy = 80, repro = 130):
      self.name = name
      self.kingdom = 'Plant'
      self.energy = energy
      self.repro = repro
  
  def act(self, critter, view):
    if len(critter) > 0:

      #REPRODUCE, if you have the energy and the space
      if (len(view.spaces) > 0) & (critter[3] > critter[4]):
       #dirRepro = spaces[random.choice(list(spaces.keys()))]
       dirRepro = random.choice(view.spaces)
       baby = {'location':dirRepro, 'energy':(-1 * critter[3] / 2), 'act':'repro'}
                    
       return baby

      #otherwise just grow a little
      else:
       growing = {'energy':10, 'act':'grow'}

       return growing
    
    else:
      return None

  def birthStats(self):
    # set plant's starting stats
    birthEn = int(self.energy + (np.random.randn(1)[0] * 20))
    birthRe = int(self.repro + (np.random.randn(1)[0] * 10))
    birthFa = 0

    # save for passing on to offspring
    inheritance = {'birthEn': birthEn, 'birthRe': birthRe, 'birthFa': birthFa}
    return [self.name, self.kingdom, inheritance, birthEn, birthRe, birthFa]
'''
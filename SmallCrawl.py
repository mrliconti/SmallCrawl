# Mr. Liconti
# May 3, 2018
# SmallCrawl.py
# Small Crawl: A small crawler game written in Python

import random #will need for random events
import numpy  #will need for joining 1D arrays into a 2D array

######################################################################################
# VARIABLES:

#room types, loot types, encounter types
room_bank = ['Hall' , 'Large Room', 'Small Room' , 'Library' , 'Conservatory' , 'Lab', 'Kitchen']
loot_bank = ['coin', 'key', 'flashlight', 'health', 'weapon', 'armour']
encounters_bank = ['BadGuy1', 'BadGuy2', 'BadGuy3', 'BadGuy4']

# Empty Arrays
map = []  #empty map array
loot = [] #empty loot array
encounters = [] #empty encounter array
######################################################################################

def generateLayout(someBank):
  randomArray = random.sample(someBank, 4) #generate map, loot, or encounters. Depends on which bank was passed
  return randomArray

def showWhatWasGenerated():
  print(map)  #proof that random map was generated
  print(loot) # proof that random loot was generated
  print(encounters) #proog that random encounters were generated

def showGame(g):
  print(g)

def generateGame(m,l,e):
  g = numpy.vstack([m, l, e])
  return g
  
map = generateLayout(room_bank) #generate the map
loot = generateLayout(loot_bank)  #generate the loot
encounters = generateLayout(encounters_bank)  #generate the encounters
game = generateGame(map, loot, encounters)  #generate the game
showGame(game)  #show the game

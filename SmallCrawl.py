# Mr. Liconti
# May 3, 2018
# SmallCrawl.py
# Small Crawl: A small crawler game written in Python

import random #will need for random events
import numpy  #will need for joining 1D arrays into a 2D array

######################################################################################
# VARIABLES

#room types, loot types, encounter types
room_bank = ['hall' , 'large room', 'small room' , 'library' , 'conservatory' , 'lab', 'kitchen']
loot_bank = ['a coin', 'a key', 'a flashlight', 'a first-aid kit', 'a weapon', 'some armour']
encounters_bank = ['Guard', 'Monster', 'Spy', 'Soldier']

# Empty Arrays
map = []  #empty map array
loot = [] #empty loot array
encounters = [] #empty encounter array
playerInventory = [] #empty inventory array
playerHP = 10 #set initial player HP
######################################################################################

def generateLayout(someBank):
  randomArray = random.sample(someBank, 4) #generate map, loot, or encounters. Depends on which bank was passed
  return randomArray

def showWhatWasGenerated():
  print(map)  #proof that random map was generated
  print(loot) # proof that random loot was generated
  print(encounters) #proof that random encounters were generated

def showGame(g):
  print(g)

def generateGame(m,l,e):
  g = numpy.vstack([m, l, e])
  return g

def showLocation(g):
  print('You are in the ' + g[0][0] + '.')

def showInventory(pi):
  print('You find ' + pi[0] + '.')
  
def addItem(pi, g):
  pi.append(g[1][2])
  return pi
  
def showEncounter(g):
  print('A ' + g[2][0] + ' is in the same area as you.')

map = generateLayout(room_bank) #generate the map
loot = generateLayout(loot_bank)  #generate the loot
encounters = generateLayout(encounters_bank)  #generate the encounters
game = generateGame(map, loot, encounters)  #generate the game
#showGame(game)  #DEBUG: show the game
showLocation(game) #show player location
playerInventory = addItem(playerInventory, game) #give player an addItem
showInventory(playerInventory)  #show player inventory
showEncounter(game)

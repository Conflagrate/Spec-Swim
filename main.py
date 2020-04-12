# note: relays account for half the points as compared to individual events

# project created for the 2020 AP CSP Create Task
# project started: April 8
# hours put in: 43 (so far)

import numpy as np
import statistics as sts
import matplotlib.pyplot as plt

from datetime import datetime
from termcolor import colored as clr

def checkOverallPlacement(swimmerPlacement, *, eventType='individual'):
  racePoints = 0
  if eventType == 'individual':
    # won the event (individual)
    if (swimmerPlacement == 1):
      racePoints = racePoints + 12

    # top 3 overall (individual)
    elif (swimmerPlacement <= 3):
      racePoints = racePoints + 8

    # top 5 overall (individual)
    elif (swimmerPlacement <= 5):
      racePoints = racePoints + 6

    # outside top 5 (individual)
    else:
      racePoints = racePoints + 0

  elif eventType == 'relay':
    # won the event (relay)
    if (swimmerPlacement == 1):
      racePoints = racePoints + 6

    # top 3 overall (relay)
    elif (swimmerPlacement <= 3):
      racePoints = racePoints + 4

    # top 5 overall (relay)
    elif (swimmerPlacement <= 5):
      racePoints = racePoints + 3

    # outside top 5 (relay)
    else:
      racePoints = racePoints + 0
    
  return float(racePoints)

def checkPercentagePlacement(swimmerPlacement, totalSwimmers, *, eventType='individual'):
  racePoints = 0
  if eventType == 'individual':
    # top 75% (individual)
    if (swimmerPlacement / totalSwimmers <= .75):
      racePoints = racePoints + 0.5

    # top 50% (individual)
    if (swimmerPlacement / totalSwimmers <= .50):
      racePoints = racePoints + 1

    # top 25% (individual)
    if (swimmerPlacement / totalSwimmers <= .25):
      racePoints = racePoints + 1.75

    # top 10% (individual)
    if (swimmerPlacement / totalSwimmers <= .10):
      racePoints = racePoints + 3

    # last place (individual)
    if (swimmerPlacement / totalSwimmers == 1):
      racePoints = racePoints - 5
  
  elif eventType == 'relay':
    # top 75% (relay)
    if (swimmerPlacement / totalSwimmers <= .75):
      racePoints = racePoints + 0.25

    # top 50% (relay)
    if (swimmerPlacement / totalSwimmers <= .50):
      racePoints = racePoints + 0.5

    # top 25% (relay)
    if (swimmerPlacement / totalSwimmers <= .25):
      racePoints = racePoints + 0.875

    # top 10% (relay)
    if (swimmerPlacement / totalSwimmers <= .10):
      racePoints = racePoints + 1.5

    # last place (relay)
    if (swimmerPlacement / totalSwimmers == 1):
      racePoints = racePoints - 5

  return float(racePoints)

swimmerName = input('Choose what swimmer to record: ')
print('')
swimTotalVar = int(input('How many races were swam?: '))

for i in range(swimTotalVar):
  print('')
  placementVar = int(input('What was the placement?: '))
  totalVar = int(input('How many swimmers swam in total?: '))
  eventVar = input('Was the event a relay or individual? (defaults to individual): ')

  if eventVar.lower() == 'relay' or eventVar.lower() == 'individual':
    eventVar = eventVar
  else:
    eventVar = 'individual'

# initialize the Swimmer class and the syntax
class Swimmer:
  def __init__(self, name, points):
    self.name = name
    self.points = points
  def calculateRacePoints(name):
    for i in range(swimTotalVar):
      racePoints = checkOverallPlacement(placementVar, eventType=eventVar) + checkPercentagePlacement(placementVar, totalVar, eventType=eventVar)
      racePoints = racePoints + racePoints
    return float(racePoints)

swimmer = Swimmer(swimmerName, Swimmer.calculateRacePoints(swimmerName)) # create the swimmer with the given specs

print('')
print(swimmer.name, 'earned', swimmer.points, 'points!')

cleanOutput = swimmer.name, swimmer.points
cleanOutput = str(cleanOutput) + '\n'

output = open('output.csv', 'a+')
output.write(cleanOutput)
output.close()
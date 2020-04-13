import datetime

import numpy as np
import statistics as sts
import matplotlib.pyplot as plt

from termcolor import colored as clr

# find the time and use it to set a timestamp
class Time(datetime.tzinfo):
  def utcoffset(self, x):
    return datetime.timedelta(hours=-5) + self.dst(x)

  def dst(self, x):
    date = datetime.datetime(x.year, 3, 8)
    self.dston = date + datetime.timedelta(days=6-date.weekday())
    date = datetime.datetime(x.year, 11, 1)
    self.dstoff = date + datetime.timedelta(days=6-date.weekday())
    if self.dston <= x.replace(tzinfo=None) < self.dstoff:
      return datetime.timedelta(hours=1)
    else:
      return datetime.timedelta(0)

  def tzname(self, x):
    return 'Time'

def getTimeStamp():
  return datetime.datetime.now(tz=Time()).strftime('%Y-%m-%d %H:%M:%S')

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
startTime = 'START:', getTimeStamp()
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

# initialize the Swimmer class
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

endTime = 'END:', getTimeStamp()

cleanOutput = startTime, endTime, swimmer.name.upper(), swimmer.points
cleanOutput = str(cleanOutput) + '\n'

output = open('output.csv', 'a+')
output.write(cleanOutput)
output.close()
import math
import datetime

from dataclasses import dataclass

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

def checkImprovement(seedTime, prelimTime, finalTime): # convert times to seconds first
  if prelimTime == finalTime:
    timeDifference = prelimTime - seedTime
  else:
    if prelimTime < finalTime:
      timeDifference = prelimTime - seedTime
    else:
      timeDifference = finalTime - seedTime
  
  timeDifference = float(timeDifference) # re-define as float for precision and accuracy

  if timeDifference >= 0:
    return (-1 * timeDifference) / 4 # for each added 0.5, net -1 point
  elif timeDifference < 0:
    return abs(timeDifference) / 4 # for each drop of 0.5, net +1 point

swimmerName = input('Choose what swimmer to record: ')
swimmerName = swimmerName.strip() # strip leading/trailing whitespace
nameLength = len(swimmerName) # save length for future formatting

startTime = 'LOGGED FROM', getTimeStamp() # get the beginning time stamp

print('')
swimTotalVar = int(input('How many races were swam?: '))

for i in range(swimTotalVar):
  print('')
  seedTime = float(input('What was the seed time (in seconds and milliseconds)?: '))
  prelimTime = float(input('What was the prelim time?: '))
  finalTime = float(input('What was the final time?: '))
  placementVar = int(input('What was the placement?: '))
  totalVar = int(input('How many swimmers swam in total?: '))
  eventVar = input('Was the event a relay or individual? (defaults to individual): ')

  if eventVar.lower() == 'relay' or eventVar.lower() == 'individual':
    eventVar = eventVar
  else:
    eventVar = 'individual'

# initialize the Swimmer class

'''
@dataclass
class Swimmer:
  name: str
  points: float

swimmer = Swimmer(swimmerName, Swimmer.calculateRacePoints(swimmerName))
'''

class Swimmer:
  def __init__(self, name, points):
    self.name = name # swimmer name
    self.points = points # swimmer points

  def calculateRacePoints(name):
    for i in range(swimTotalVar): # repeat for number of races
      racePoints = checkOverallPlacement(placementVar, eventType=eventVar) + checkPercentagePlacement(placementVar, totalVar, eventType=eventVar) + checkImprovement(seedTime, prelimTime, finalTime) # calculate points based on all factors
      racePoints = racePoints + racePoints # originally set at '0' so need to add racePoints again

    return float(racePoints)

swimmer = Swimmer(swimmerName, Swimmer.calculateRacePoints(swimmerName)) # create the swimmer with the given specs

print('')
print(swimmer.name, 'earned', int(math.ceil(swimmer.points)), 'points!') # raw format (math.ceil() to round up regardless of decimal)

endTime = 'TO', getTimeStamp()

cleanOutput = startTime, endTime, swimmer.name.upper(), int(math.ceil(swimmer.points)), 'POINTS'
cleanOutput = str(cleanOutput) + '\n' # convert to string for easy file writing

for removal in "(,')": # don't want any ugly characters
  cleanOutput = cleanOutput.replace(removal, '') # replace unwanted characters with a blank spot

indexOfOutput = 0 # unnecessary variable? refactor later

# format the output in a more readable manner
cleanOutput = cleanOutput[:(indexOfOutput + 12)] + '[' + cleanOutput[indexOfOutput + 12:]
cleanOutput = cleanOutput[:(indexOfOutput + 32)] + ']' + cleanOutput[indexOfOutput + 32:]
cleanOutput = cleanOutput[:(indexOfOutput + 37)] + '[' + cleanOutput[indexOfOutput + 37:]
cleanOutput = cleanOutput[:(indexOfOutput + 57)] + ']' + cleanOutput[indexOfOutput + 57:]
cleanOutput = cleanOutput[:(indexOfOutput + 59)] + '[' + cleanOutput[indexOfOutput + 59:]
cleanOutput = cleanOutput[:(59 + nameLength + 1)] + ']' + cleanOutput[59 + nameLength + 1:] # add 1 as output fix
cleanOutput = cleanOutput[:(59 + nameLength + 2)] + ':' + cleanOutput[59 + nameLength + 2:] # add 2 to directly follow ']'

output = open('output.csv', 'a+') # 'a+' to create file and prevent errors if file is not found
output.write(cleanOutput) # append output
output.close() # close file
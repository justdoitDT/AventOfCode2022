# import data
import re
with open('/Users/dthomas/Downloads/input16.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
for index in range(len(lines)):
    lines[index] = re.split(r'Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve |, ', lines[index])[1:]
#print(lines)


# define Valve class
class Valve(object):
    def __init__(self, input):
        self.name = input[0]
        self.flowRate = int(input[1])
        self.neighbors = []
        for neighbor in input[2:]:
            self.neighbors.append(neighbor)
        self.isOpen = self.getFlowRate() == 0
        # self.nearestClosed = float('inf')
        self.potential = 0
        self.neighborPotentials = []
    def getName(self):
        return self.name
    def getFlowRate(self):
        return self.flowRate
    def getNeighbors(self):
        return self.neighbors
    def getIsOpen(self):
        return self.isOpen
    def open(self):
        self.isOpen = True
    def close(self):
        self.isOpen = False
    def setPotential(self, potential):
        self.potential = potential
    def getPotential(self):
        return self.potential
    def getNeighborPotentials(self):
        return self.neighborPotentials


# establish hashmap of valves
valvesDict = {}
for valve in lines:
    valvesDict[valve[0]] = Valve(valve)


# breadth first search function to determine length of shortest distance from each valve to each other valve
def shortestPath(startingValve, targetValve):
    visited = set([])
    queue = [(startingValve, 0)]    # [(currentValve, distance from valve)]
    while queue:
        currentValve = queue.pop(0)
        if currentValve[0] == targetValve:
            return currentValve[1]
        visited.add(currentValve[0])
        for neighbor in valvesDict[currentValve[0]].getNeighbors():
            if neighbor not in visited:
                queue.append((neighbor, currentValve[1] + 1))


# memoize shortest distances between valves
distancesDict = {}      # {'AA':{'CA':3, }}
for startingValve in valvesDict:
    distancesDict[startingValve] = {}
    for targetValve in valvesDict:
        distancesDict[startingValve][targetValve] = shortestPath(startingValve, targetValve)


# create closedValves, a set of closed valves
closedValves = set([])
for valve in valvesDict:
    if valvesDict[valve].getFlowRate() > 0:
        closedValves.add(valve)



# Part One

# initialize output
maxPressure = [(0, [])]

# define depth first search, visit closed valves in all possible orders
def dfs(currentValve, visitedSet, elapsedTime, pressureReleased, visitedList):
    # stop condition
    if elapsedTime > 28:
        # update maximum pressureReleased
        if pressureReleased > maxPressure[0][0]:
            maxPressure[0] = (pressureReleased, visitedList)
        # return one level up
        return
    # open currentValve and move to next closed valve
    for valve in closedValves:
        if valve not in visitedSet:
            dfs(valve, set(list(visitedList) + [valve]), elapsedTime + 1 + distancesDict[valve][currentValve], pressureReleased + valvesDict[currentValve].getFlowRate() * (29 - elapsedTime), visitedList + [valve])
    # return one level up
    return


dfs('AA', set(['AA']), -1, 0, ['AA'])    # start elapsedTime at -1 because the algorithm wastes 1 minute opening AA

print('Part One final answer', maxPressure[0])


























'''
# failed Part Two solution: loop wayyyy too slow. 15 factorial can't be done.

import itertools

# initialize output
maxPressure = 0

# check every order of valves
perms = list(itertools.permutations(closedValves))
lenPerms = len(perms)
permCount = 0
for perm in perms:
    permCount += 1
    print(permCount / lenPerms, '%  complete')
    releasedThisRun = {'AA':[], 'UH':[], 'KZ':[], 'IP':[], 'EB':[], 'IS':[], 'BH':[], 'RW':[], 'IF':[], 'ZZ':[], 'MT':[], 'SI':[], 'NH':[], 'ZQ':[], 'WG':[], 'AO':[]}
    # go through my path (forwards through perm)
    myCurrentValve = 'AA'
    myTime = -1     # start myTime at -1 because the algorithm wastes 1 minute opening AA
    myIndex = -1    # start myIndex at -1 because the it starts at 'AA' before moving to the 0th valve
    while myTime < 25:
        # spend 1 minute opening myCurrentValve
        myTime += 1
        # update pressure released
        releasedThisRun[myCurrentValve].append(valvesDict[myCurrentValve].getFlowRate() * (26 - myTime))
        # move to next valve
        myTime += distancesDict[myCurrentValve][perm[myIndex + 1]]
        myIndex += 1
        myCurrentValve = perm[myIndex]
    # go through elephant's path (backwards through perm)
    elephantCurrentValve = 'AA'
    elephantTime = -1
    elephantIndex = 0
    while elephantTime < 25:
        # spend 1 minute opening elephantCurrentValve
        elephantTime += 1
        # update pressure released
        releasedThisRun[elephantCurrentValve].append(valvesDict[elephantCurrentValve].getFlowRate() * (26 - elephantTime))
        # move to next valve
        elephantTime += distancesDict[elephantCurrentValve][perm[elephantIndex + 1]]
        elephantIndex -= 1
        elephantCurrentValve = perm[elephantIndex]
    # calculate total pressure released for this perm
    sumPressure = 0
    for valve in releasedThisRun:
        sumPressure += max(releasedThisRun[valve])
    if sumPressure > maxPressure:
        maxPressure = sumPressure

print(maxPressure)
'''












'''
# failed attempt at Part Two. takes ~75 days.
import itertools

# initialize output
maxPressure = (0, [])
count = 0

# create empty dictionary to draw copies from later
defaultPressureDict = {}
for valve in closedValves:
    defaultPressureDict[valve] = 0
# print(defaultPressureDict)

# try every order of valves
perms = itertools.permutations(closedValves)
lenPerms = 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2
for perm in perms:

    # track progress
    count += 1
    if count % 1000000 == 0:
        print(count / lenPerms * 100, '%  complete. Best so far: ', maxPressure)

    # reset pressureDict
    pressureDict = defaultPressureDict.copy()

    # tally my contributions
    current = 0
    elapsedTime = distancesDict['AA'][perm[current]]
    while elapsedTime < 29:
        pressureDict[perm[current]] = (29 - elapsedTime) * valvesDict[perm[current]].getFlowRate()
        elapsedTime += distancesDict[perm[current]][perm[current + 1]]
        current += 1

    # tally elephant's contributions
    current = 14
    elapsedTime = distancesDict['AA'][perm[current]]
    while elapsedTime < 29:
        pressureDict[perm[current]] = max(pressureDict[perm[current]], (29 - elapsedTime) * valvesDict[perm[current]].getFlowRate())
        elapsedTime += distancesDict[perm[current]][perm[current - 1]]
        current -= 1

    if sum(pressureDict.values()) > maxPressure[0]:
        maxPressure = (sum(pressureDict.values()), perm)



print(maxPressure)
'''








'''
Part Two failed solution. loop, too slow.
import itertools

# initialize output
maxPressure = 0
count = 0

# try every order of valves
perms = itertools.permutations(closedValves)
lenPerms = 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2
for perm in perms:
    count += 1
    if count % 1000000 == 0:
        print(count / lenPerms * 100, '%  complete. Best so far: ', maxPressure)
    valves = ['AA'] + list(perm) + ['AA']
    # reset starting parameters
    elapsedTime = -1
    pressureReleased = 0
    myCurrent = 0
    elephantCurrent = 16
    mySteps = 0
    elephantSteps = 0
    # loop until every valve visited or time is up
    while myCurrent < elephantCurrent and elapsedTime < 29:

        # open valve(s)
        # if only I have just arrived at my next valve
        if mySteps == 0 and elephantSteps > 0:
            # open my valve
            pressureReleased += valvesDict[valves[myCurrent]].getFlowRate() * (29 - elapsedTime)
            elapsedTime += 1
        # if only the elephant has just arrived at its next valve
        elif elephantSteps == 0 and mySteps > 0:
            # open elephant's valve
            pressureReleased += valvesDict[valves[myCurrent]].getFlowRate() * (29 - elapsedTime)
            elapsedTime += 1
        # if we both have just arrived at our next valves
        elif mySteps == 0 and elephantSteps == 0:
            # open both valves
            pressureReleased += valvesDict[valves[myCurrent]].getFlowRate() * (29 - elapsedTime)
            pressureReleased += valvesDict[valves[myCurrent]].getFlowRate() * (29 - elapsedTime)
            elapsedTime += 1

        # advance to next valve(s)
        # if I'm closer to my next valve
        if distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps < distancesDict[valves[elephantCurrent]][valves[elephantCurrent - 1]] - elephantSteps:
            # advance me to my next valve
            myCurrent += 1
            mySteps = 0
            # step elephant toward its next valve
            elephantSteps += distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps
            elapsedTime += distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps
        # if elephant is closer to its next valve
        elif distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps > distancesDict[valves[elephantCurrent]][valves[elephantCurrent - 1]] - elephantSteps:
            # advance elephant to its next valve
            elephantCurrent -= 1
            elephantSteps = 0
            # step me toward my next valve
            mySteps += distancesDict[valves[elephantCurrent]][valves[elephantCurrent - 1]] - elephantSteps
            elapsedTime += distancesDict[valves[elephantCurrent]][valves[elephantCurrent - 1]] - elephantSteps
        # if elephant and I are equidistant from our next valves
        elif distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps == distancesDict[valves[elephantCurrent]][valves[elephantCurrent - 1]] - elephantSteps:
            # advance both of us to our next valve
            myCurrent += 1
            mySteps = 0
            elephantCurrent -= 1
            elephantSteps = 0
            elapsedTime += distancesDict[valves[myCurrent]][valves[myCurrent + 1]] - mySteps

    # corner case where elephant and I both arrive at our last node at the same time
    if myCurrent == elephantCurrent and elapsedTime < 29:
        # open last valve
        pressureReleased += valvesDict[valves[myCurrent]].getFlowRate() * (29 - elapsedTime)

    # update maxPressure
    if pressureReleased > maxPressure:
        maxPressure = pressureReleased

print(maxPressure)
'''





'''
# Part Two failed solution. DFS within DFS, too slow.

# initialize output
totalMaxPressure = [(0, [])]

# define depth first search, visit closed valves in all possible orders
def myDFS(currentValve, visitedSet, elapsedTime, pressureReleased, visitedList):

    def elephantDFS(currentValve, visitedSet, elapsedTime, pressureReleased, visitedList):
        # stop condition
        if elapsedTime > 28:
            # update maximum pressureReleased and return
            if pressureReleased > elephantMaxPressure[0][0]:
                elephantMaxPressure[0] = (pressureReleased, visitedList)
            # return one level up
            return
        # open currentValve and move to next closed valve
        for valve in closedValves:
            if valve not in visitedSet:
                elephantDFS(valve, set(list(visitedList) + [valve]),
                            elapsedTime + 1 + distancesDict[valve][currentValve],
                            pressureReleased + valvesDict[currentValve].getFlowRate() * (29 - elapsedTime),
                            visitedList + [valve])
        # return one level up
        return

    # stop condition
    if elapsedTime > 28:
        # run elephantDFS
        elephantMaxPressure = [(0, [])]
        elephantDFS('AA', visitedSet, -1, 0, ['AA'])  # start elapsedTime at -1 because the algorithm wastes 1 minute opening AA
        print('me', (pressureReleased, visitedList), 'elephantMaxPressure', elephantMaxPressure)
        # update maximum pressureReleased
        if pressureReleased + elephantMaxPressure[0][0] > totalMaxPressure[0][0]:
            totalMaxPressure[0] = (pressureReleased + elephantMaxPressure[0][0], visitedList, elephantMaxPressure[0][1])
        # return one level up
        return
    # open currentValve and move to next closed valve
    for valve in closedValves:
        if valve not in visitedSet:
            myDFS(valve, set(list(visitedList) + [valve]), elapsedTime + 1 + distancesDict[valve][currentValve], pressureReleased + valvesDict[currentValve].getFlowRate() * (29 - elapsedTime), visitedList + [valve])
    # return one level up
    return



myDFS('AA', set(['AA']), -1, 0, ['AA'])    # start elapsedTime at -1 because the algorithm wastes 1 minute opening AA

print('final answer', totalMaxPressure[0])
'''
















# way too slow
'''
import itertools

# most valves visitable: 10
# potential issue: spending a minute at an already open valve

maxPressureReleased = 0
# try every order
for combination in itertools.combinations(closedValves, 11):
    for myPlan in list(itertools.permutations(combination)):
        for elephantPlan in list(itertools.permutations(combination)):

            # reset open valves
            for valve in closedValves:
                valvesDict[valve].close()
            # reset starting variables
            elapsedTime = 3     # because 1 minute is wasted opening 'AA'
            pressureReleased = 0
            # set starting positions
            myPlan = ['AA'] + list(myPlan)
            elephantPlan = ['AA'] + list(elephantPlan)
            myCurrentValve = 0
            elephantCurrentValve = 0
            # we both start with a cooldown, we won't be our first closed valve at the start
            myCooldown = 0
            elephantCooldown = 0

            # loop until time is up
            while elapsedTime < 28:
                print('elapsedTime', elapsedTime, 'myCurrentValve', myCurrentValve, 'myCooldown', myCooldown)

                # execute my move
                # if I am still waiting on cooldown
                if myCooldown > 0:
                    myCooldown -= 1
                # if cooldown is over
                else:
                    # if myCurrentValve is not yet open
                    if not valvesDict[myPlan[myCurrentValve]].getIsOpen():
                        # open valve and update pressureReleased
                        valvesDict[myPlan[myCurrentValve]].open()
                        pressureReleased += valvesDict[myPlan[myCurrentValve]].getFlowRate() * (29 - elapsedTime)
                    # if myCurrentValve already open
                    else:
                        # set cooldown to open next valve
                        myCooldown = distancesDict[myPlan[myCurrentValve]][myPlan[myCurrentValve + 1]]
                        # advance to next valve
                        myCurrentValve += 1

                # execute elephant's move
                # if elephant is still waiting on cooldown
                if elephantCooldown > 0:
                    elephantCooldown -= 1
                # if cooldown is over
                else:
                    # if elephantCurrentValve is not open
                    if not valvesDict[elephantPlan[elephantCurrentValve]].getIsOpen():
                        # open valve and update pressureReleased
                        valvesDict[elephantPlan[elephantCurrentValve]].open()
                        pressureReleased += valvesDict[elephantPlan[elephantCurrentValve]].getFlowRate() * (29 - elapsedTime)
                    # if elephantCurrentValve already open
                    else:
                        # set cooldown to open next valve
                        elephantCooldown = distancesDict[elephantPlan[elephantCurrentValve]][elephantPlan[elephantCurrentValve + 1]]
                        # advance to next valve
                        elephantCurrentValve += 1

                # advance elapsedTime
                elapsedTime += 1

            # time is up
            if pressureReleased > maxPressureReleased:
                maxPressureReleased = pressureReleased

    #         break
    #     break
    # break

print('final answer', maxPressureReleased)
'''





























# failed Part One attempt using "potentials" for every valve (even open ones), choosing which direction to go based on highest "potential"
'''
# define function to refresh potentials map
def updatePotentials(elapsedTime):
    for valve in valvesDict:
        valvesDict[valve].potential = 0
        for openValve in shortestPathsDict:
            if not valvesDict[openValve].getIsOpen():
                valvesDict[valve].potential += max(0, valvesDict[openValve].getFlowRate() * (29 - elapsedTime - shortestPathsDict[openValve][valve]))
    for valve in valvesDict:
        valvesDict[valve].neighborPotentials = []
        for neighbor in valvesDict[valve].getNeighbors():
            valvesDict[valve].neighborPotentials.append((valvesDict[neighbor].getPotential(), neighbor))
        valvesDict[valve].neighborPotentials.sort()
        valvesDict[valve].neighborPotentials = valvesDict[valve].neighborPotentials[::-1]

updatePotentials(0)

def printPotentials(valve = None):
    if valve:
        print(valve, 'potential =', valvesDict[valve].getPotential(), 'neighbors', valvesDict[valve].getNeighborPotentials())
        return
    for valve in valvesDict:
        print(valve, 'potential =', valvesDict[valve].getPotential(), 'neighbors', valvesDict[valve].getNeighborPotentials())

#printPotentials()

elapsedTime = 0
currentValve = 'AA'
visitedSinceOpening = []
pressureReleased = 0
while elapsedTime < 29:
    visitedSinceOpening.append(currentValve)
    print(currentValve, elapsedTime)
    printPotentials(currentValve)
    # open this valve if closed and has higher potential than its neighboring valves
    if not valvesDict[currentValve].getIsOpen() and valvesDict[currentValve].getPotential() > valvesDict[currentValve].getNeighborPotentials()[-1][0]:
        # open valve
        valvesDict[currentValve].open()
        elapsedTime += 1
        pressureReleased += valvesDict[currentValve].getFlowRate() * (30 - elapsedTime)
        visitedSinceOpening = []
        print('open valve', valve, 'flowRate:', valvesDict[valve].getFlowRate(), 'total released:', pressureReleased)
        # update potentials
        updatePotentials(elapsedTime)
        printPotentials(currentValve)
    # move to next valve
    for (potential, neighbor) in valvesDict[currentValve].getNeighborPotentials():
        print(neighbor)
        if neighbor not in visitedSinceOpening:
            currentValve = neighbor
            break
    elapsedTime += 1

print(pressureReleased)
'''







# failed Part One approach: visit highest potential node, then new highest potential node, etc.
# incorrect result  -  path: ['AA', 'KZ', 'RW', 'IS', 'WG', 'NH', 'IP'], total pressure released: 1364
'''
# create closedValves, a set of closed valves
closedValves = set([])
for valve in valvesDict:
    if valvesDict[valve].getFlowRate() > 0:
        closedValves.add(valve)

# define function to refresh potentials map
def updatePotentials(elapsedTime, currentValve):
    for valve in valvesDict:
        valvesDict[valve].setPotential(0)
        if valve in closedValves:
            valvesDict[valve].setPotential(max(0, valvesDict[valve].getFlowRate() * (29 - elapsedTime - shortestPath(currentValve, valve))))

updatePotentials(0, 'AA')


# follow path from starting point to each subsequent highest potential remaining closed valve

# include 'AA' in closedValves so it can be popped after the first iteration
closedValves.add('AA')

# initialize starting variables
pressureReleased = 0
elapsedTime = -1    # because 1 minute is wasted opening 'AA'
currentValve = 'AA'
path = []

# loop until out of time
while elapsedTime < 29:

    # record path
    path.append(currentValve)

    # open currentValve
    valvesDict[currentValve].open()
    elapsedTime += 1
    pressureReleased += valvesDict[currentValve].getFlowRate() * (30 - elapsedTime)
    print('open valve', currentValve, 'flowRate:', valvesDict[currentValve].getFlowRate(), 'total released:', pressureReleased, 'elapsedT time:', elapsedTime)

    # update closedValves and potentials
    closedValves.remove(currentValve)
    updatePotentials(elapsedTime, currentValve)

    # find highest potential remaining closed valve
    nextValve = (-float('inf'), None)
    for closedValve in closedValves:
        if valvesDict[closedValve].getPotential() > nextValve[0]:
            nextValve = (valvesDict[closedValve].getPotential(), closedValve)
    # set nextValve to the highest potential remaining closed valve
    nextValve = nextValve[1]
    # move to nextValve
    elapsedTime += shortestPath(currentValve, nextValve)
    currentValve = nextValve

print('\npath:', path, 'total pressure released:', pressureReleased)
'''


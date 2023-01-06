import re

# import data
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
    def getPotential(self):
        return self.potential
    def getNeighborPotentials(self):
        return self.neighborPotentials


# establish hashmap of valves
valvesDict = {}
for valve in lines:
    valvesDict[valve[0]] = Valve(valve)

# determine length of shortest path from each closed valve to each other valve
# breadth first search
def shortestPath(valve, targetValve):
    visited = set([])
    queue = [(valve, 0)]    # [(currentValve, distance from valve)]
    while True:
        currentValve = queue.pop(0)
        if currentValve[0] == targetValve:
            return currentValve[1]
        visited.add(currentValve[0])
        for neighbor in valvesDict[currentValve[0]].getNeighbors():
            if neighbor not in visited:
                queue.append((neighbor, currentValve[1] + 1))
# generate dictionary of shortest paths to each other valve starting from the 15 valves with positive flow rates
shortestPathsDict = {}
for valve in valvesDict:
    if valvesDict[valve].getFlowRate() > 0:
        shortestPathsDict[valve] = {}
        for targetValve in valvesDict:
            shortestPathsDict[valve][targetValve] = shortestPath(valve, targetValve)




# brute force approach (takes almost 90 days to run)

# create closedValves, an ordered set of closed valves
closedValvesList = []
closedValves = {}
for valve in shortestPathsDict:
    closedValvesList.append(((30 - shortestPathsDict[valve]['AA']) * valvesDict[valve].getFlowRate(), valve))
closedValvesList.sort()
closedValvesList = closedValvesList[::-1]
for (potential, valve) in closedValvesList:
    closedValves[valve] = None

# initialize output and counter
maxPressure = [(0, [])]
permsTried = [0]

# define depth first search, visit closed valves in all possible orders
def dfs(currentValve, visitedSet, elapsedTime, pressureReleased, visitedList):
    # stop condition
    if elapsedTime > 28:
        permsTried[0] += 1
        if permsTried[0] % 1000000 == 0:
            print('permsTried', permsTried[0], 'currentPath', visitedList, 'maxPressure', maxPressure[0])
        if pressureReleased > maxPressure[0][0]:
            maxPressure[0] = (pressureReleased, visitedList)
            return
    # open currentValve and move to next closed valve
    for valve in closedValves:
        if valve not in visitedSet:
            dfs(valve, set(list(visitedList) + [valve]), elapsedTime + 1 + shortestPathsDict[valve][currentValve], pressureReleased + valvesDict[currentValve].getFlowRate() * (29 - elapsedTime), visitedList + [valve])

    return


dfs('AA', set(['AA']), -1, 0, ['AA'])    # start elapsedTime at -1 because the algorithm wastes 1 minute opening AA

print('final answer', maxPressure[0])







# failed attempt using "potentials", choosing which direction to go based on highest "potential"
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

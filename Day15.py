import re

# import data
with open('/Users/dthomas/Downloads/input15.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
for index in range(len(lines)):
    lines[index] = re.split(r'Sensor at x=|, y=|: closest beacon is at x=', lines[index])[1:]

# organize data into a dictionary {sensorCoord(x, y): closestBeaconCoord(x, y))}
sensorsDict = {}
for line in lines:
    sensorsDict[(int(line[0]), int(line[1]))] = (int(line[2]), int(line[3]))

# define helper function, returns manhattan distance between two input coordinates
def measureDist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])



'''
# Part One

def mergeRanges(existingRanges, newRange):
    # no existing ranges
    if not existingRanges:
        return [newRange]
    # yes existing ranges
    replacementRange = []
    output = []
    existingRanges.sort(key = lambda x: x[0])
    noOverlap = True
    for existingRange in existingRanges:
        # if existingRange doesn't overlap with newRange
        if max(newRange) < min(existingRange) or min(newRange) > max(existingRange):
            output.append(existingRange)
            # if overlapped ranges are waiting to be added
            if replacementRange:
                output.append(replacementRange[-1])
                # empty replacementRange
                replacementRange = []
        # if existingRange overlaps with newRange
        else:
            newRange = range(min(min(newRange), min(existingRange)), max(max(newRange) + 1, max(existingRange) + 1))
            replacementRange.append(newRange)
            # adjust flag
            noOverlap = False
    # if overlapped ranges are waiting to be added
    if replacementRange:
        output.append(replacementRange[-1])
    if noOverlap:
        output.append(newRange)
    output.sort(key = lambda x: x[0])
    return output

blocked = []
for sensor in sensorsDict:
    # calculate radius
    radius = measureDist(sensor, sensorsDict[sensor])
    if sensor[1] - radius < 2000000 < sensor[1] + radius:
        print('sensor', sensor, 'radius', radius)
        distTo2000000 = abs(2000000 - sensor[1])
        positionsToCancel = radius - distTo2000000
        print(blocked)
        print('newRange', range(sensor[0] - positionsToCancel, sensor[0] + positionsToCancel))
        blocked = mergeRanges(blocked, range(sensor[0] - positionsToCancel, sensor[0] + positionsToCancel))
        print(blocked, '\n')

output = 0
for eachRange in blocked:
    output += len(eachRange) + 1

# account for sensors and beacons in the exclusion zone
excSensBeacs = set([])
for sensor in sensorsDict:
    if sensor[1] == 2000000:
        for eachRange in blocked:
            if sensor[0] in eachRange:
                excSensBeacs.add(sensor)
    if sensorsDict[sensor][1] == 2000000:
        for eachRange in blocked:
            if sensorsDict[sensor][0] in eachRange:
                excSensBeacs.add(sensorsDict[sensor])
for sensBeac in excSensBeacs:
    output -= 1

print(output)
'''



# Part Two

# find the edges of each sensor's radius

# check each edge coordinate (x, y), looking for one that has other edge
# coordinates at (x - 1, y + 1), (x + 1, y + 1), and (x, y + 2)
# the coordinate below this edge coordinate is likely to be the one available coordinate

edges = []
intersections = set([])
sensorCount = 0
for (x, y) in sensorsDict:
    edges.append(set([]))
    print('sensor ' + str(sensorCount) + '/' + str(len(sensorsDict)), (x, y))
    # calculate radius
    radius = measureDist((x, y), sensorsDict[(x, y)])
    for y_increment in range(radius + 1):
        x_increment = radius - y_increment
        newEdges = [(x + x_increment, y + y_increment), (x + x_increment, y - y_increment), (x - x_increment, y + y_increment), (x - x_increment, y - y_increment)]
        for newEdge in newEdges:
            for index, edgesSet in enumerate(edges):
                if newEdge in edgesSet:
                    intersections.add((newEdge, index, sensorCount))
                edges[-1].add(newEdge)
    sensorCount += 1

print('lenEdges', len(edges))
print('lenIntersections', len(intersections))
print(intersections)

'''
candidates = set([])
numIntersections = len(intersections)
edgeCount = 0
print(numIntersections)

for (x, y) in intersections:
    if len(candidates) > 5:
        break
    edgeCount += 1
    if edgeCount % 100 == 0:
        print('Progress: ' + str(edgeCount/numIntersections*100) + '%')
    if (x - 1, y + 1) in edges and (x + 1, y + 1) in edges and (x, y + 2) in edges and (x, y + 1) not in edges:
        candidates.add((x, y + 1))

print(candidates)
'''
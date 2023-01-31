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
# for sensor in sensorsDict:
#     print(sensor, sensorsDict[sensor])

# define helper function, returns manhattan distance between two input coordinates
def measureDist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])





# Part One
'''
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

# Strategy:
# each sensor is surrounded by a diamond-shaped exclusion zone
# the distress beacon must lie at the intersection of the 1-pixel-wide gap between
    # the top-right edge of one exclusion zone, and the bottom-left edge of another exclusion zone
    # and
    # the top-left edge of one exclusion zone, and the bottom-right edge of another exclusion zone



# define LineSegment class
# inputs are coordinates of 2 endpoints
# (note: top-left and bottom-right diamond segments are defined to have negative slope)     y = mx + b
class LineSegment(object):
    def __init__(self, endpoint1, endpoint2):   # (x1, y1), (x2, y2)
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2
        self.slope = (endpoint2[1] - endpoint1[1]) / (endpoint2[0] - endpoint1[0])
        self.y_int = endpoint1[1] - self.getSlope() * endpoint1[0]
        self.x_min = min(endpoint1[0], endpoint2[0])
        self.x_max = max(endpoint1[0], endpoint2[0])
        self.domain = [self.getXmin(), self.getXmax]    # [x_min, x_max]
    def getEndpoints(self):
        endpoints = [self.endpoint1, self.endpoint2]
        endpoints.sort()
        return endpoints
    def getSlope(self):
        return self.slope
    def getYint(self):
        return self.y_int
    def getXmin(self):
        return self.x_min
    def getXmax(self):
        return self.x_max
    def getDomain(self):
        return self.domain
    def __str__(self):
        return 'slope: '+ str(self.getSlope()) + '  y-int: ' + str(self.getYint()) + '\nendpoints: ' + str(self.getEndpoints()[0]) + ', ' + str(self.getEndpoints()[1])



# define sensor class
# calculates and stores the 4 edges of sensor's exclusion zone as LineSegment objects
class Sensor(object):
    def __init__(self, identifier, sensorCoord, closestBeacon):
        self.ID = 'Sensor # ' + str(identifier)
        self.coord = sensorCoord
        self.x = sensorCoord[0]
        self.y = sensorCoord[1]
        self.beacon = closestBeacon
        self.radius = measureDist(sensorCoord, closestBeacon)
        self.topRightEdge = LineSegment((self.x + self.radius, self.y), (self.x, self.y - self.radius))
        self.topLeftEdge = LineSegment((self.x, self.y - self.radius), (self.x - self.radius, self.y))
        self.bottomLeftEdge = LineSegment((self.x - self.radius, self.y), (self.x, self.y + self.radius))
        self.bottomRightEdge = LineSegment((self.x, self.y + self.radius), (self.x + self.radius, self.y))
    def getID(self):
        return self.ID
    def getCoord(self):
        return self.coord
    def getBeacon(self):
        return self.beacon
    def getRadius(self):
        return self.radius
    def getTopRightEdge(self):
        return self.topRightEdge
    def getTopLeftEdge(self):
        return self.topLeftEdge
    def getBottomLeftEdge(self):
        return self.bottomLeftEdge
    def getBottomRightEdge(self):
        return self.bottomRightEdge
    def __str__(self):
        return self.ID + ' ' + str(self.getCoord()) + ' Radius: ' + str(self.getRadius())



# create list of all sensors
sensorsList = []
count = 0
for sensor in sensorsDict:
    sensorsList.append(Sensor(count, sensor, sensorsDict[sensor]))
    count += 1



# find the 1-pixel-wide gap between the top-right edge of one exclusion zone, and the bottom-left edge of another exclusion zone
segmentAboveGap = None
for sensor1 in sensorsList:
    for sensor2 in sensorsList:
        # if y-intercepts of edges differ by 2
        if abs(sensor1.getBottomLeftEdge().getYint() - sensor2.getTopRightEdge().getYint()) == 2:
            # if there is overlap between the ranges
            if not (sensor1.getBottomLeftEdge().getXmax() < sensor2.getTopRightEdge().getXmin() or sensor1.getBottomLeftEdge().getXmin() > sensor2.getTopRightEdge().getXmax()):
                segmentAboveGap = sensor1.getBottomLeftEdge()
                break
    if segmentAboveGap:
        break

# create posGapSegment representing the 1-pixel-wide gap between the top-right and bottom-left edges of two exclusion zones
# get endpoints of segmentAboveGap
[(ep1x, ep1y), (ep2x, ep2y)] = segmentAboveGap.getEndpoints()
# endpoints of gap segment are 1 pixel below endpoints of segmentAboveGap
posGapSegment = LineSegment((ep1x, ep1y + 1), (ep2x, ep2y + 1))



# find the 1-pixel-wide gap between the top-left edge of one exclusion zone, and the bottom-right edge of another exclusion zone
segmentAboveGap = None
for sensor1 in sensorsList:
    for sensor2 in sensorsList:
        # if y-intercepts of edges differ by 2
        if abs(sensor1.getTopLeftEdge().getYint() - sensor2.getBottomRightEdge().getYint()) == 2:
            # if there is overlap between the ranges
            if not (sensor1.getTopLeftEdge().getXmax() < sensor2.getBottomRightEdge().getXmin() or sensor1.getTopLeftEdge().getXmin() > sensor2.getBottomRightEdge().getXmax()):
                segmentAboveGap = sensor2.getBottomRightEdge()
                break
            if segmentAboveGap:
                break

# create negGapSegment representing the 1-pixel-wide gap between the top-left and bottom-right edges of two exclusion zones
# get endpoints of segmentAboveGap
[(ep1x, ep1y), (ep2x, ep2y)] = segmentAboveGap.getEndpoints()
# endpoints of gap segment are 1 pixel below endpoints of segmentAboveGap
negGapSegment = LineSegment((ep1x, ep1y + 1), (ep2x, ep2y + 1))



# distress beacon lies at the intersection of posGapSegment and negGapSegment
# Algebra to solve for (x, y) coordinates of intersection point
#
#     y = m1 * x + b1 = m2x + b2
#         m1 * x + b1 = m2x + b2
#       x * (m1 - m2) = b2 - b1
#                   x = (b2 - b1) / (m1 - m2)
#                   y = m1 * x + b1

xDistress = (negGapSegment.getYint() - posGapSegment.getYint()) / (posGapSegment.getSlope() - negGapSegment.getSlope())
yDistress = posGapSegment.getSlope() * xDistress + posGapSegment.getYint()



# calculate tuning frequency
tuningFrequency = 4000000 * xDistress + yDistress
print(tuningFrequency)

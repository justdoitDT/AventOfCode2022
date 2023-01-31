with open('/Users/dthomas/Downloads/input17.txt') as f:
    lines = f.readlines()
jetPattern = lines[0]
lenJetPattern = len(jetPattern)



# Doesn't work. Not sure why. Looks like it does, but the result is incorrect.


# Day One

# define Rock class
class Rock(object):
    def __init__(self, shape, towerHeight):
        self.shape = shape
        if shape == 'flat':
            self.coords = [[2, towerHeight + 4], [3, towerHeight + 4], [4, towerHeight + 4], [5, towerHeight + 4]]
            self.topSegment = 0
        elif shape == 'plus':
            self.coords = [[2, towerHeight + 5], [3, towerHeight + 4], [3, towerHeight + 5], [3, towerHeight + 6], [4, towerHeight + 5]]
            self.topSegment = 3
        elif shape == 'revL':
            self.coords = [[2, towerHeight + 4], [3, towerHeight + 4], [4, towerHeight + 4], [4, towerHeight + 5], [4, towerHeight + 6]]
            self.topSegment = 4
        elif shape == 'vert':
            self.coords = [[2, towerHeight + 4], [2, towerHeight + 5], [2, towerHeight + 6], [2, towerHeight + 7]]
            self.topSegment = 3
        elif shape == 'square':
            self.coords = [[2, towerHeight + 4], [2, towerHeight + 5], [3, towerHeight + 4], [3, towerHeight + 5]]
            self.topSegment = 1

    def getShape(self):
        return self.shape

    def getCoords(self):
        return self.coords

    def getTopSegment(self):
        return self.topSegment

    def getTop(self):
        return self.getCoords()[self.getTopSegment()][1]

    def moveDown(self, maxHeight, stoppedRocks):
        '''
        :param maxHeight: int. highest occupied height
        :param stoppedRocks: set of coordinates occupied by stopped rocks
        :return: tuple. (True/False, maxHeight, stoppedRocks)    True if rock moved down, False if rock couldn't be moved down
        '''
        # check if rock is unable to fall
        # for each segment
        for (x, y) in self.getCoords():
            # if segment only 1 unit above obstacle, the rock can't fall
            if (x, y - 1) in stoppedRocks:
                # add all coords to stoppedRocks
                for coord in self.getCoords():
                    stoppedRocks.add(tuple(coord))
                print('Reached the bottom.', self.getCoords())
                return (False, max(maxHeight, self.getTop()), stoppedRocks)
        # if the rock can fall
        for coordIndex in range(len(self.getCoords())):
            self.coords[coordIndex][1] -= 1
        print('Moved down.', self.getCoords())
        return (True, maxHeight, stoppedRocks)

    def moveLeft(self, stoppedRocks):
        # for each segment
        canMoveLeft = True
        # if segment is all the way to the left, or coordinate to the left is blocked
        for (x, y) in self.getCoords():
            if x == 0 or (x - 1, y) in stoppedRocks:
                canMoveLeft = False
        if canMoveLeft:
            # move each segment one unit to the left
            for coordIndex in range(len(self.getCoords())):
                self.coords[coordIndex][0] -= 1
            print('Moved left.', self.getCoords())
        else:
            print('Failed to move left.', self.getCoords())

    def moveRight(self, stoppedRocks):
        canMoveRight = True
        # for each segment
        for (x, y) in self.getCoords():
            # if segment is all the way to the right, or coordinate to the right is blocked
            if x == 6 or (x + 1, y) in stoppedRocks:
                canMoveRight = False
        if canMoveRight:
            # move each segment one unit to the right
            for coordIndex in range(len(self.getCoords())):
                self.coords[coordIndex][0] += 1
            print('Moved right.', self.getCoords())
        else:
            print('Failed to move right.', self.getCoords())


# initialize variables
rocks = ['flat', 'plus', 'revL', 'vert', 'square']
maxHeight = 0
stoppedRocks = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
rockCount = 0
jetPatternIndex = 0
maxHeights = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # for visual debugging

# drop 2022 rocks
while rockCount < 2022:
    currentRock = Rock(rocks[rockCount % 5], maxHeight)
    print('\nrockCount', rockCount, currentRock.getShape(), currentRock.getCoords())
    stillFalling = True
    # loop until rock can't be moved down
    while stillFalling:
        # jet of gas pushes rock
        if jetPattern[jetPatternIndex % lenJetPattern] == '<':
            currentRock.moveLeft(stoppedRocks)
        else:
            currentRock.moveRight(stoppedRocks)
        jetPatternIndex += 1
        # rock falls (if it can)
        stillFalling, maxHeight, stoppedRocks = currentRock.moveDown(maxHeight, stoppedRocks)
    rockCount += 1

    # visual (for debugging)
    chamber = []
    for i in range(maxHeight + 1):
        chamber.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    for (x, y) in stoppedRocks:
        chamber[y][x] = 'X'
    for (x, y) in currentRock.getCoords():
        chamber[y][x] = 'O'
        if y > maxHeights[x][1]:
            maxHeights[x][0] = maxHeights[x][1]
            maxHeights[x][1] = y
    count = maxHeight
    for i in chamber[::-1]:
        print(i, count)
        count -= 1
        # # cut off printing below unreachable space
        # if count < min(maxHeights)[0]:
        #     break



print(maxHeight)
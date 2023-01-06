with open('/Users/dthomas/Downloads/input12.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
stepsGrid = []
for line in lines:
    stepsGrid.append([])
    for char in line:
        stepsGrid[-1].append(float('inf'))


# create dict to convert heights from letters to numbers
heightDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, \
              'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}


# memoization
lenLines = len(lines)
widthLines = len(lines[0])



'''
# Part One

# set starting and ending locations
lines[20] = 'a' + lines[20][1:91] + 'z' + lines[20][92:]
stepsGrid[20][0] = 0


# execute breadth-first search

queue = [(20, 0)]   # (row, col)
while queue:
    current = queue.pop(0)
    print(current)
    # check up
    # if we're not already at the top row
    # and if this is the quickest path to the above coordinate
    # and if the above coordinate is a reachable height
    if current[0] > 0 \
    and stepsGrid[current[0] - 1][current[1]] > stepsGrid[current[0]][current[1]] + 1 \
    and heightDict[lines[current[0] - 1][current[1]]] <= heightDict[lines[current[0]][current[1]]] + 1:
        # set number of steps to above coordinate
        stepsGrid[current[0] - 1][current[1]] = stepsGrid[current[0]][current[1]] + 1
        # add above coordinate to queue
        queue.append((current[0] - 1, current[1]))

    # check down
    # if we're not already at the bottom row
    # and if this is the quickest path to the below coordinate
    # and if the below coordinate is a reachable height
    if current[0] < lenLines - 1 \
    and stepsGrid[current[0] + 1][current[1]] > stepsGrid[current[0]][current[1]] + 1 \
    and heightDict[lines[current[0] + 1][current[1]]] <= heightDict[lines[current[0]][current[1]]] + 1:
        # set number of steps to above coordinate
        stepsGrid[current[0] + 1][current[1]] = stepsGrid[current[0]][current[1]] + 1
        # add above coordinate to queue
        queue.append((current[0] + 1, current[1]))

    # check left
    # if we're not already at the left-most column
    # and if this is the quickest path to the left coordinate
    # and if the left coordinate is a reachable height
    if current[1] > 0 \
    and stepsGrid[current[0]][current[1] - 1] > stepsGrid[current[0]][current[1]] + 1 \
    and heightDict[lines[current[0]][current[1] - 1]] <= heightDict[lines[current[0]][current[1]]] + 1:
        # set number of steps to above coordinate
        stepsGrid[current[0]][current[1] - 1] = stepsGrid[current[0]][current[1]] + 1
        # add above coordinate to queue
        queue.append((current[0], current[1] - 1))

    # check right
    # if we're not already at the right-most column
    # and if this is the quickest path to the right coordinate
    # and if the right coordinate is a reachable height
    if current[1] < widthLines - 1 \
    and stepsGrid[current[0]][current[1] + 1] > stepsGrid[current[0]][current[1]] + 1 \
    and heightDict[lines[current[0]][current[1] + 1]] <= heightDict[lines[current[0]][current[1]]] + 1:
        # set number of steps to above coordinate
        stepsGrid[current[0]][current[1] + 1] = stepsGrid[current[0]][current[1]] + 1
        # add above coordinate to queue
        queue.append((current[0], current[1] + 1))

print(stepsGrid[20][91])
'''




# Part Two
import copy

# create template stepsGrid to be deep copied
stepsGridPerm = copy.deepcopy(stepsGrid)

# set starting and ending locations
lines[20] = 'a' + lines[20][1:91] + 'z' + lines[20][92:]
startingLocations = []
for row in range(lenLines):
    for col in range(widthLines):
        if lines[row][col] == 'a':
            startingLocations.append((row, col))


# execute breadth-first search starting from each coordinate in startingLocations
minSteps = []
for coordinate in startingLocations:
    stepsGrid = copy.deepcopy(stepsGridPerm)
    stepsGrid[coordinate[0]][coordinate[1]] = 0
    queue = [coordinate]   # (row, col)
    while queue:
        current = queue.pop(0)
        # check up
        # if we're not already at the top row
        # and if this is the quickest path to the above coordinate
        # and if the above coordinate is a reachable height
        if current[0] > 0 \
        and stepsGrid[current[0] - 1][current[1]] > stepsGrid[current[0]][current[1]] + 1 \
        and heightDict[lines[current[0] - 1][current[1]]] <= heightDict[lines[current[0]][current[1]]] + 1:
            # set number of steps to above coordinate
            stepsGrid[current[0] - 1][current[1]] = stepsGrid[current[0]][current[1]] + 1
            # add above coordinate to queue
            queue.append((current[0] - 1, current[1]))
        # check down
        # if we're not already at the bottom row
        # and if this is the quickest path to the below coordinate
        # and if the below coordinate is a reachable height
        if current[0] < lenLines - 1 \
        and stepsGrid[current[0] + 1][current[1]] > stepsGrid[current[0]][current[1]] + 1 \
        and heightDict[lines[current[0] + 1][current[1]]] <= heightDict[lines[current[0]][current[1]]] + 1:
            # set number of steps to above coordinate
            stepsGrid[current[0] + 1][current[1]] = stepsGrid[current[0]][current[1]] + 1
            # add above coordinate to queue
            queue.append((current[0] + 1, current[1]))
        # check left
        # if we're not already at the left-most column
        # and if this is the quickest path to the left coordinate
        # and if the left coordinate is a reachable height
        if current[1] > 0 \
        and stepsGrid[current[0]][current[1] - 1] > stepsGrid[current[0]][current[1]] + 1 \
        and heightDict[lines[current[0]][current[1] - 1]] <= heightDict[lines[current[0]][current[1]]] + 1:
            # set number of steps to above coordinate
            stepsGrid[current[0]][current[1] - 1] = stepsGrid[current[0]][current[1]] + 1
            # add above coordinate to queue
            queue.append((current[0], current[1] - 1))
        # check right
        # if we're not already at the right-most column
        # and if this is the quickest path to the right coordinate
        # and if the right coordinate is a reachable height
        if current[1] < widthLines - 1 \
        and stepsGrid[current[0]][current[1] + 1] > stepsGrid[current[0]][current[1]] + 1 \
        and heightDict[lines[current[0]][current[1] + 1]] <= heightDict[lines[current[0]][current[1]]] + 1:
            # set number of steps to above coordinate
            stepsGrid[current[0]][current[1] + 1] = stepsGrid[current[0]][current[1]] + 1
            # add above coordinate to queue
            queue.append((current[0], current[1] + 1))
    # record length of shortest path to destination
    minSteps.append(stepsGrid[20][91])


print(min(minSteps))

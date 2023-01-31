import copy


# import data
with open('/Users/dthomas/Downloads/input24.txt') as f:
    valley = f.readlines()
for index, line in enumerate(valley):
    valley[index] = line[:-1]

# testing
valley = ['#.######', '#>>.<^<#', '#.<..<<#', '#>v.><>#', '#<^v^^>#', '######.#']



# memoize valley parameters
minRow = 1
maxRow = len(valley) - 2
minCol = 1
maxCol = len(valley[0]) - 2


# organize data into a hashmap with an entry for each coordinate in the valley, and create emptyValley to be copied later
valleyDict = {(0, 1):['.']}
emptyValley = {(0, 1):['.']}
for rowIndex in range(1, maxRow + 1):
    for colIndex in range(1, maxCol + 1):
        valleyDict[(rowIndex, colIndex)] = [valley[rowIndex][colIndex]]
        emptyValley[(rowIndex, colIndex)] = ['.']



# memoize valley arrangement after each minute (first 369 minutes)
# initialize valleyArrangements
valleyArrangements = {0:copy.deepcopy(valleyDict)}
# initialize elapsedTime
elapsedTime = 0
# create dictionary of blizzard shapes and their corresponding [row, col] modifications
blizzardDict = {'^':[-1, 0], 'v':[1, 0], '<':[0, -1], '>':[0, 1]}
# iterate through 370 minutes of valley arrangements
while elapsedTime < 370:
    elapsedTime += 1
    # advance blizzards by 1 minute
    newValley = copy.deepcopy(emptyValley)
    # iterate through each coordinate
    for row, col in valleyDict:
        # pop each individual blizzard located at coordinate
        while valleyDict[(row, col)]:
            currentBlizzard = valleyDict[(row, col)].pop()
            # don't bother with '.', they are contained within emptyValley and will be replenished automatically
            if currentBlizzard == '.':
                continue
            # check which way blizzard will move
            rowMod, colMod = blizzardDict[currentBlizzard]
            # push blizzard to its new row
            newRow = row + rowMod
            # wrap if necessary
            if newRow < minRow:
                newRow = maxRow
            elif newRow > maxRow:
                newRow = minRow
            # push blizzard to its new col
            newCol = col + colMod
            # wrap if necessary
            if newCol < minCol:
                newCol = maxCol
            elif newCol > maxCol:
                newCol = minCol
            # add new coordinate of blizzard to newValley
            newValley[(newRow, newCol)].append(currentBlizzard)
    # memoize arrangement
    valleyArrangements[elapsedTime] = copy.deepcopy(newValley)
    # prepare for next iteration
    valleyDict = copy.deepcopy(newValley)
print('valley arrangements memoized')



# define a dfs, take every possible path
def dfs(currentRow, currentCol, elapsedTime, path):
    print((currentRow, currentCol), 'time', elapsedTime, path)
    # stop condition: can't possibly beat fastest time or pre-imposed maxTime limit
    if elapsedTime + (maxRow - currentRow) + (maxCol - minCol) >= min(minElapsedTime[0], maxTime[0]):
        print('giving up')
        newPromisingPaths.append((currentRow, currentCol, elapsedTime, path))
        return

    # stop condition: successfully reached destination
    if (currentRow, currentCol) == (4, 6): #(25, 120):                       # testing (4, 6):
        # check if current path was the fastest so far
        if elapsedTime + 1 < minElapsedTime[0]:
            minElapsedTime[0] = elapsedTime + 1
            minElapsedTime[1] = path
            # shift flag to stop iteration
            solutionsFound[0] += 1
        print('\nelapsedTime', elapsedTime, ' position', (currentRow, currentCol),
              '       minElapsedTime', minElapsedTime[0], ' path', minElapsedTime[1], '\n')
        # return up to check other paths
        return

    # try moving right
    if currentRow > 0 and currentCol < maxCol and valleyArrangements[elapsedTime + 1][(currentRow, currentCol + 1)] == ['.']:
        dfs(currentRow, currentCol + 1, elapsedTime + 1, path + [(currentRow, currentCol)])
    # try moving down
    if currentRow < maxRow and valleyArrangements[elapsedTime + 1][(currentRow + 1, currentCol)] == ['.']:
        dfs(currentRow + 1, currentCol, elapsedTime + 1, path + [(currentRow, currentCol)])
    # try standing still
    if valleyArrangements[elapsedTime + 1][(currentRow, currentCol)] == ['.']:
        dfs(currentRow, currentCol, elapsedTime + 1, path + [(currentRow, currentCol)])
    # try moving up
    if currentRow > 0 and currentRow > minRow + 1 and valleyArrangements[elapsedTime + 1][(currentRow - 1, currentCol)] == ['.']:
        dfs(currentRow - 1, currentCol, elapsedTime + 1, path + [(currentRow, currentCol)])
    # try moving left
    if currentRow > 0 and currentCol > minCol + 1 and valleyArrangements[elapsedTime + 1][(currentRow, currentCol - 1)] == ['.']:
        dfs(currentRow, currentCol - 1, elapsedTime + 1, path + [(currentRow, currentCol)])
    # can't move or stand still; return up to check other paths
    print(valleyArrangements[elapsedTime + 1])
    print('cant move or stay')
    return


# define function to print numbers more clearly
def printNum(num):
    numString = str(num)
    output = ''
    # memoize length of numString
    lenNum = len(str(numString))
    for i in range(lenNum):
        output += numString[lenNum - 1 - i]
        if i % 3 == 2 and i < lenNum - 1:
            output += ','
    return output[::-1]




# check every possible path that takes less than maxTime minutes, then increment maxTime

# initialize pre-imposed maxTime limit
maxTime = [1] #change back to 145
# memoize paths that were abandoned due to the pre-imposed maxTime limit
promisingPaths = [(0, 1, 0, [])]    # (startingRow, startingCol, elapsedTime, [path_coord1, path_coord2, ..., ])
# initialize minimum elapsed time to traverse the valley
minElapsedTime = [float('inf'), 'path']
# set flag to stop iteration
solutionsFound = [0]

# iterate until solution is found
while solutionsFound[0] < 1:
    # reset newPromisingPaths
    newPromisingPaths = []
    # memoize number of stems in promisingPaths
    lenPromisingPaths = len(promisingPaths)
    print('maxTime: ' + str(maxTime[0]) + '  ' + printNum(lenPromisingPaths) + ' stems remaining')
    # execute DFS starting from each stem in promisingPaths
    for stemIndex in range(lenPromisingPaths):
        startRow, startCol, startTime, startPath = promisingPaths[stemIndex]
        dfs(startRow, startCol, startTime, startPath)
        # print progress
        if (lenPromisingPaths - stemIndex ) % 1000000 == 0:
            print('maxTime: ' + str(maxTime[0]) + '  ' + printNum(lenPromisingPaths - stemIndex) + ' stems remaining')
    # increment maxTime and prepare for next iteration
    maxTime[0] += 1
    promisingPaths = newPromisingPaths.copy()






# wrong guesses
# 444 too high
# 369 too high
# import data
with open('/Users/dthomas/Downloads/input23.txt') as f:
    field = f.readlines()
for index, line in enumerate(field):
    field[index] = line[:-1]



# Part One (successful)
'''
# count the elves, initialize and populate list to store current position of each elf
elfCount = 0
newElfPositions = []
for rowIndex in range(len(field)):
    for colIndex in range(len(field[0])):
        if field[rowIndex][colIndex] == '#':
            elfCount += 1
            newElfPositions.append((rowIndex, colIndex))


# define directions and initialize at North
directions = ['N', 'S', 'W', 'E']
directionsIndex = 0


# define function to check if an elf has neighbors
def hasNeighbors(row, col, elfPositions):
    for rowAdj in [-1, 0, 1]:
        for colAdj in [-1, 0, 1]:
            if rowAdj == colAdj == 0:
                continue
            if (row + rowAdj, col + colAdj) in elfPositions:
                return True
    return False


# loop for 10 rounds
roundsCompleted = 0
while roundsCompleted < 10:
    elfPositions = newElfPositions.copy()
    print('roundsCompleted', roundsCompleted)
    # empty out data structures to record elves' proposed moves
    proposedMovesDict = {}
    proposedMovesList = []
    # iterate through all elves
    for elfNum in range(elfCount):
        # memoize current elf's row and col
        row, col = elfPositions[elfNum]
        if not hasNeighbors(row, col, elfPositions):
            proposedMovesList.append(None)
            continue
        # initialize canMove and proposedCoord lists
        canMove = []    # list of bools, describing whether elf can move in each of the cardinal directions
        possibleMoves = []  # list of proposed moves, one in each cardinal direction from starting position
        # check North
        canMove.append((row - 1, col) not in elfPositions and (row - 1, col - 1) not in elfPositions and (row - 1, col + 1) not in elfPositions)
        possibleMoves.append((row - 1, col))
        # check South
        canMove.append((row + 1, col) not in elfPositions and (row + 1, col - 1) not in elfPositions and (row + 1, col + 1) not in elfPositions)
        possibleMoves.append((row + 1, col))
        # check West
        canMove.append((row, col - 1) not in elfPositions and (row - 1, col - 1) not in elfPositions and (row + 1, col - 1) not in elfPositions)
        possibleMoves.append((row, col - 1))
        # check East
        canMove.append((row, col + 1) not in elfPositions and (row - 1, col + 1) not in elfPositions and (row + 1, col + 1) not in elfPositions)
        possibleMoves.append((row, col + 1))
        # propose moving in first valid direction
        dirCount = 0
        # iterate through each cardinal direction (starting direction rotates)
        while dirCount < 4:
            # if current direction is legal
            if canMove[(directionsIndex + dirCount) % 4]:
                # include proposed move in proposedMovesDict
                if possibleMoves[(directionsIndex + dirCount) % 4] in proposedMovesDict:
                    proposedMovesDict[possibleMoves[(directionsIndex + dirCount) % 4]] += 1
                else:
                    proposedMovesDict[possibleMoves[(directionsIndex + dirCount) % 4]] = 1
                # include proposed move in proposedMovesDict (indexed to each individual elf)
                proposedMovesList.append(possibleMoves[(directionsIndex + dirCount) % 4])
                # stop checking the other directions
                break
            # advance to next direction if moving in current direction was not legal
            dirCount += 1
        # if no directions are legal, append None to proposedMovesList
        if not canMove[0] and not canMove[1] and not canMove[2] and not canMove[3]:
            proposedMovesList.append(None)
    # move the elves that can move
    newElfPositions = []
    for elfNum in range(elfCount):
        # if current elf has proposed a move, and its proposed coordinate is unique
        if proposedMovesList[elfNum] and proposedMovesDict[proposedMovesList[elfNum]] == 1:
            # move elf to its proposed coordinate
            newElfPositions.append(proposedMovesList[elfNum])
        else:
            newElfPositions.append(elfPositions[elfNum])
    # prepare for next round
    directionsIndex += 1
    roundsCompleted += 1


# determine size of smallest rectangle containing all elves
elfPositions = newElfPositions
minRow = float('inf')
maxRow = -float('inf')
minCol = float('inf')
maxCol = -float('inf')
for elfNum in range(elfCount):
    row, col = elfPositions[elfNum]
    if row < minRow:
        minRow = row
    if row > maxRow:
        maxRow = row
    if col < minCol:
        minCol = col
    if col > maxCol:
        maxCol = col

# count empty space in rectangle
print((maxRow - minRow + 1) * (maxCol - minCol + 1) - elfCount)
'''





# Part Two

# count the elves, initialize and populate list to store current position of each elf
elfCount = 0
newElfPositions = []
for rowIndex in range(len(field)):
    for colIndex in range(len(field[0])):
        if field[rowIndex][colIndex] == '#':
            elfCount += 1
            newElfPositions.append((rowIndex, colIndex))


# define directions and initialize at North
directions = ['N', 'S', 'W', 'E']
directionsIndex = 0


# define function to check if an elf has neighbors
def hasNeighbors(row, col, elfPositions):
    for rowAdj in [-1, 0, 1]:
        for colAdj in [-1, 0, 1]:
            if rowAdj == colAdj == 0:
                continue
            if (row + rowAdj, col + colAdj) in elfPositions:
                return True
    return False


# loop until elves stop moving
roundsCompleted = 0
elvesMoved = True
while elvesMoved:
    elvesMoved = False
    elfPositions = newElfPositions.copy()
    print('roundsCompleted', roundsCompleted)
    # empty out data structures to record elves' proposed moves
    proposedMovesDict = {}
    proposedMovesList = []
    # iterate through all elves
    for elfNum in range(elfCount):
        # memoize current elf's row and col
        row, col = elfPositions[elfNum]
        if not hasNeighbors(row, col, elfPositions):
            proposedMovesList.append(None)
            continue
        # initialize canMove and proposedCoord lists
        canMove = []    # list of bools, describing whether elf can move in each of the cardinal directions
        possibleMoves = []  # list of proposed moves, one in each cardinal direction from starting position
        # check North
        canMove.append((row - 1, col) not in elfPositions and (row - 1, col - 1) not in elfPositions and (row - 1, col + 1) not in elfPositions)
        possibleMoves.append((row - 1, col))
        # check South
        canMove.append((row + 1, col) not in elfPositions and (row + 1, col - 1) not in elfPositions and (row + 1, col + 1) not in elfPositions)
        possibleMoves.append((row + 1, col))
        # check West
        canMove.append((row, col - 1) not in elfPositions and (row - 1, col - 1) not in elfPositions and (row + 1, col - 1) not in elfPositions)
        possibleMoves.append((row, col - 1))
        # check East
        canMove.append((row, col + 1) not in elfPositions and (row - 1, col + 1) not in elfPositions and (row + 1, col + 1) not in elfPositions)
        possibleMoves.append((row, col + 1))
        # propose moving in first valid direction
        dirCount = 0
        # iterate through each cardinal direction (starting direction rotates)
        while dirCount < 4:
            # if current direction is legal
            if canMove[(directionsIndex + dirCount) % 4]:
                # include proposed move in proposedMovesDict
                if possibleMoves[(directionsIndex + dirCount) % 4] in proposedMovesDict:
                    proposedMovesDict[possibleMoves[(directionsIndex + dirCount) % 4]] += 1
                else:
                    proposedMovesDict[possibleMoves[(directionsIndex + dirCount) % 4]] = 1
                # include proposed move in proposedMovesDict (indexed to each individual elf)
                proposedMovesList.append(possibleMoves[(directionsIndex + dirCount) % 4])
                # stop checking the other directions
                break
            # advance to next direction if moving in current direction was not legal
            dirCount += 1
        # if no directions are legal, append None to proposedMovesList
        if not canMove[0] and not canMove[1] and not canMove[2] and not canMove[3]:
            proposedMovesList.append(None)
    # move the elves that can move
    newElfPositions = []
    for elfNum in range(elfCount):
        # if current elf has proposed a move, and its proposed coordinate is unique
        if proposedMovesList[elfNum] and proposedMovesDict[proposedMovesList[elfNum]] == 1:
            # move elf to its proposed coordinate
            newElfPositions.append(proposedMovesList[elfNum])
            elvesMoved = True
        else:
            newElfPositions.append(elfPositions[elfNum])
    # prepare for next round
    directionsIndex += 1
    roundsCompleted += 1


print(roundsCompleted)

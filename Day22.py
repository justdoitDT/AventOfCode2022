# import data
with open('/Users/dthomas/Downloads/input22.txt') as f:
    board = f.readlines()
for index, line in enumerate(board):
    board[index] = line[:-1]
path = board[-1] + 'S'  # add 'S' as a stop sign at the end of path
board = board[:-2]


# memoize length of path
lenPath = len(path)


# define Row and Col classes

class Row(object):
    def __init__(self, rowIndex, rowContents):
        self.rowIndex = rowIndex
        try:
            self.minColIndex = min(rowContents.index('.'), rowContents.index('#'))
        except ValueError:
            self.minColIndex = rowContents.index('.')
        self.maxColIndex = len(rowContents) - 1
        self.rowContents = rowContents
    def getRowIndex(self):
        return self.rowIndex
    def getMinColIndex(self):
        return self.minColIndex
    def getMaxColIndex(self):
        return self.maxColIndex
    def getRowContents(self):
        return self.rowContents

class Col(object):
    def __init__(self, colIndex, colContents):
        self.colIndex = colIndex
        try:
            self.minRowIndex = min(colContents.index('.'), colContents.index('#'))
        except ValueError:
            self.minRowIndex = colContents.index('.')
        self.maxRowIndex = len(colContents) - 1
        self.colContents = colContents
    def getRowIndex(self):
        return self.colIndex
    def getMinRowIndex(self):
        return self.minRowIndex
    def getMaxRowIndex(self):
        return self.maxRowIndex
    def getColContents(self):
        return self.colContents






# Part One


# create Row object for each row, store in hashmap
rowsDict = {}
for index, row in enumerate(board):
    rowsDict[index] = Row(index, row)


# create Col object for each col, store in hashmap
colsDict = {}
for colIndex in range(len(board[0])):
    colContents = ''
    for rowIndex in range(len(board)):
        try:
            colContents += (board[rowIndex][colIndex])
        except IndexError:
            break
    colsDict[colIndex] = Col(colIndex, colContents)



# set starting position and direction
row, col = 0, rowsDict[0].getMinColIndex()
directions = ['R', 'D', 'L', 'U']
directionIndex = 0


# initialize pointers to traverse path
trailPointer = 0
leadPointer = 0


# traverse path
while trailPointer < lenPath:
    # advance leadPointer until it reaches a letter
    while path[leadPointer] not in {'L', 'R', 'S'}:     # 'S' means stop, it's the last character in path
        leadPointer += 1
    # move tiles
    # if facing right
    if directions[directionIndex] == 'R':
        for _ in range(int(path[trailPointer : leadPointer])):  # this can be done faster by advancing to last open tile, instead of incrementing one tile at a time
            # check one tile to the right
            newCol = col + 1
            # wrap, if necessary
            if newCol > rowsDict[row].getMaxColIndex():
                newCol = rowsDict[row].getMinColIndex()
            # if tile is blocked, stop advancing
            if rowsDict[row].getRowContents()[newCol] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                col = newCol
    # if facing left
    elif directions[directionIndex] == 'L':
        for _ in range(int(path[trailPointer : leadPointer])):  # this can be done faster by advancing to last open tile, instead of incrementing one tile at a time
            # check one tile to the left
            newCol = col - 1
            # wrap, if necessary
            if newCol < rowsDict[row].getMinColIndex():
                newCol = rowsDict[row].getMaxColIndex()
            # if tile is blocked, stop advancing
            if rowsDict[row].getRowContents()[newCol] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                col = newCol
    # if facing up
    elif directions[directionIndex] == 'U':
        for _ in range(int(path[trailPointer : leadPointer])):  # this can be done faster by advancing to last open tile, instead of incrementing one tile at a time
            # check one tile above
            newRow = row - 1
            # wrap, if necessary
            if newRow < colsDict[col].getMinRowIndex():
                newRow = colsDict[col].getMaxRowIndex()
            # if tile is blocked, stop advancing
            if colsDict[col].getColContents()[newRow] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row = newRow
    # if facing down
    elif directions[directionIndex] == 'D':
        for _ in range(int(path[trailPointer : leadPointer])):  # this can be done faster by advancing to last open tile, instead of incrementing one tile at a time
            # check one tile above
            newRow = row + 1
            # wrap, if necessary
            if newRow > colsDict[col].getMaxRowIndex():
                newRow = colsDict[col].getMinRowIndex()
            # if tile is blocked, stop advancing
            if colsDict[col].getColContents()[newRow] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row = newRow
    # change direction
    if path[leadPointer] == 'R':
        directionIndex = (directionIndex + 1) % 4
    elif path[leadPointer] == 'L':
        directionIndex = (directionIndex - 1) % 4
    # advance pointers
    leadPointer += 1
    trailPointer = leadPointer


# calculate final password
print(1000 * (row + 1) + 4 * (col + 1) + directionIndex)







# Part Two


# define SquareRow and SquareCol classes

class SquareRow(Row):
    # wrapRight and wrapLeft are tuples (row, col, directionIndex)
    def setWrapRight(self, wrapRight):
        self.wrapRight = wrapRight
    def getWrapRight(self):
        return self.wrapRight
    def setWrapLeft(self, wrapLeft):
        self.wrapLeft = wrapLeft
    def getWrapLeft(self):
        return self.wrapLeft

class SquareCol(Col):
    # wrapTop and wrapBottom are tuples (row, col, directionIndex)
    def setWrapTop(self, wrapTop):
        self.wrapTop = wrapTop
    def getWrapTop(self):
        return self.wrapTop
    def setWrapBottom(self, wrapBottom):
        self.wrapBottom = wrapBottom
    def getWrapBottom(self):
        return self.wrapBottom



# create Row object for each row, store in hashmap, set wrap coordinates & direction
rowsDict = {}
for index, row in enumerate(board):
    rowsDict[index] = SquareRow(index, row)
    if 0 <= index < 50:
        rowsDict[index].setWrapRight((149 - index, 99, 2))
        rowsDict[index].setWrapLeft((149 - index, 0, 0))
    elif 50 <= index < 100:
        rowsDict[index].setWrapRight((49, index + 50, 3))
        rowsDict[index].setWrapLeft((100, index - 50, 1))
    elif 100 <= index < 150:
        rowsDict[index].setWrapRight((149 - index, 149, 2))
        rowsDict[index].setWrapLeft((149 - index, 50, 0))
    elif 150 <= index < 200:
        rowsDict[index].setWrapRight((149, index - 100, 3))
        rowsDict[index].setWrapLeft((0, index - 100, 1))

# create Col object for each col, store in hashmap
colsDict = {}
for colIndex in range(len(board[0])):
    colContents = ''
    for rowIndex in range(len(board)):
        try:
            colContents += (board[rowIndex][colIndex])
        except IndexError:
            break
    colsDict[colIndex] = SquareCol(colIndex, colContents)
    if 0 <= colIndex < 50:
        colsDict[colIndex].setWrapTop((50 + colIndex, 50, 0))
        colsDict[colIndex].setWrapBottom((0, 100 + colIndex, 1))
    elif 50 <= colIndex < 100:
        colsDict[colIndex].setWrapTop((100 + colIndex, 0, 0))
        colsDict[colIndex].setWrapBottom((100 + colIndex, 49, 2))
    elif 100 <= colIndex < 150:
        colsDict[colIndex].setWrapTop((199, colIndex - 100, 3))
        colsDict[colIndex].setWrapBottom((colIndex - 50, 99, 2))


# set starting position and direction
row, col = 0, rowsDict[0].getMinColIndex()
directions = ['R', 'D', 'L', 'U']
directionIndex = 0


# initialize pointers to traverse path
trailPointer = 0
leadPointer = 0


# traverse path
while trailPointer < lenPath:
    # advance leadPointer until it reaches a letter
    while path[leadPointer] not in {'L', 'R', 'S'}:     # 'S' means stop, it's the last character in path
        leadPointer += 1
    # determine how many tiles to move
    tilesToMove = int(path[trailPointer : leadPointer])
    while tilesToMove > 0:
        # if facing right
        if directions[directionIndex] == 'R':
            # check one tile to the right
            newRow = row
            newCol = col + 1
            newDir = directionIndex
            # wrap, if necessary
            if newCol > rowsDict[row].getMaxColIndex():
                newRow, newCol, newDir = rowsDict[row].getWrapRight()
            # if tile is blocked, stop advancing
            if rowsDict[newRow].getRowContents()[newCol] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row, col, directionIndex = newRow, newCol, newDir
                tilesToMove -= 1
        # if facing left
        elif directions[directionIndex] == 'L':
            # check one tile to the left
            newRow = row
            newCol = col - 1
            newDir = directionIndex
            # wrap, if necessary
            if newCol < rowsDict[row].getMinColIndex():
                newRow, newCol, newDir = rowsDict[row].getWrapLeft()
                # if tile is blocked, stop advancing
            if rowsDict[newRow].getRowContents()[newCol] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row, col, directionIndex = newRow, newCol, newDir
                tilesToMove -= 1
        # if facing up
        elif directions[directionIndex] == 'U':
            # check one tile above
            newRow = row - 1
            newCol = col
            newDir = directionIndex
            # wrap, if necessary
            if newRow < colsDict[col].getMinRowIndex():
                newRow, newCol, newDir = colsDict[col].getWrapTop()
            # if tile is blocked, stop advancing
            if colsDict[newCol].getColContents()[newRow] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row, col, directionIndex = newRow, newCol, newDir
                tilesToMove -= 1
        # if facing down
        elif directions[directionIndex] == 'D':
            # check one tile below
            newRow = row + 1
            newCol = col
            newDir = directionIndex
            # wrap, if necessary
            if newRow > colsDict[col].getMaxRowIndex():
                newRow, newCol, newDir = colsDict[col].getWrapBottom()
            # if tile is blocked, stop advancing
            if colsDict[newCol].getColContents()[newRow] == '#':
                break
            # if tile is not blocked, advance to tile
            else:
                row, col, directionIndex = newRow, newCol, newDir
                tilesToMove -= 1
    # change direction
    if path[leadPointer] == 'R':
        directionIndex = (directionIndex + 1) % 4
    elif path[leadPointer] == 'L':
        directionIndex = (directionIndex - 1) % 4
    # advance pointers
    leadPointer += 1
    trailPointer = leadPointer


# calculate final password
print(1000 * (row + 1) + 4 * (col + 1) + directionIndex)

with open('/Users/dthomas/Downloads/input8.txt') as f:
    lines = f.readlines()
trees = []
for index, line in enumerate(lines):
    trees.append(list(line[:-1]))
for rowIndex in range(len(trees)):
    for colIndex in range(len(trees[0])):
        trees[rowIndex][colIndex] = int(trees[rowIndex][colIndex])
# print(trees)




# Part One
count = 0

# check each row from left to right
for rowIndex in range(len(trees)):
    currentMax = -1
    for colIndex in range(len(trees[0])):
        # if current tree is visible
        if abs(trees[rowIndex][colIndex]) > currentMax:
            # change currentMax to the current tree's height
            currentMax = abs(trees[rowIndex][colIndex])
            # if the current tree has not already been counted
            if trees[rowIndex][colIndex] >= 0:
                # count the tree
                count += 1
                # mark the tree as counted by making it negative
                trees[rowIndex][colIndex] = -trees[rowIndex][colIndex]

# check each row from right to left
for rowIndex in range(len(trees)):
    currentMax = -1
    for colIndex in range(len(trees[0]))[::-1]:
        # if current tree is visible
        if abs(trees[rowIndex][colIndex]) > currentMax:
            # change currentMax to the current tree's height
            currentMax = abs(trees[rowIndex][colIndex])
            # if the current tree has not already been counted
            if trees[rowIndex][colIndex] >= 0:
                # count the tree
                count += 1
                # mark the tree as counted by making it negative
                trees[rowIndex][colIndex] = -trees[rowIndex][colIndex]

# check each column from top to bottom
for colIndex in range(len(trees[0])):
    currentMax = -1
    for rowIndex in range(len(trees)):
        # if current tree is visible
        if abs(trees[rowIndex][colIndex]) > currentMax:
            # change currentMax to the current tree's height
            currentMax = abs(trees[rowIndex][colIndex])
            # if the current tree has not already been counted
            if trees[rowIndex][colIndex] >= 0:
                # count the tree
                count += 1
                # mark the tree as counted by making it negative
                trees[rowIndex][colIndex] = -trees[rowIndex][colIndex]

# check each column from bottom to top
for colIndex in range(len(trees[0])):
    currentMax = -1
    for rowIndex in range(len(trees))[::-1]:
        # if current tree is visible
        if abs(trees[rowIndex][colIndex]) > currentMax:
            # change currentMax to the current tree's height
            currentMax = abs(trees[rowIndex][colIndex])
            # if the current tree has not already been counted
            if trees[rowIndex][colIndex] >= 0:
                # count the tree
                count += 1
                # mark the tree as counted by making it negative
                trees[rowIndex][colIndex] = -trees[rowIndex][colIndex]

print(count)




# Part Two

# make all trees positive again
for rowIndex in range(len(trees)):
    for colIndex in range(len(trees[0])):
        trees[rowIndex][colIndex] = abs(trees[rowIndex][colIndex])


# measure scenic score for each tree
maxScore = 0
for rowIndex in range(len(trees)):
    for colIndex in range(len(trees[0])):
        # look up
        upDist = 0
        for row in range(rowIndex)[::-1]:
            upDist += 1
            if trees[row][colIndex] >= trees[rowIndex][colIndex]:
                break
        # look down
        downDist = 0
        for row in range(rowIndex + 1, len(trees)):
            downDist += 1
            if trees[row][colIndex] >= trees[rowIndex][colIndex]:
                break
        # look left
        leftDist = 0
        for col in range(colIndex)[::-1]:
            leftDist += 1
            if trees[rowIndex][col] >= trees[rowIndex][colIndex]:
                break
        # look right
        rightDist = 0
        for col in range(colIndex + 1, len(trees[0])):
            rightDist += 1
            if trees[rowIndex][col] >= trees[rowIndex][colIndex]:
                break
        # calculate scenic score
        maxScore = max(maxScore, upDist * downDist * leftDist * rightDist)

print(maxScore)

# failed! :(

with open('/Users/dthomas/Downloads/input13.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
print(lines)


def isRightOrder(leftSide, rightSide):
    # if answer already found, return
    if output:
        return

    # loop until leftSide fully explored
    n = 0
    while n < len(leftSide):

        # if answer already found, return
        if output:
            return

        # consider first item in leftSide and rightSide
        left = leftSide[n]
        try:
            right = rightSide[n]
        # if rightSide runs out before leftSide, wrong order
        except:
            output.append(False)
            return

        print(left, '--VS--', right)

        # left and right are ints
        if type(left) == int and type(right) == int:
            if left < right:
                output.append(True)
                return
            if right < left:
                output.append(False)
                return

        # left and right are lists
        if type(left) == list and type(right) == list:
            if left and not right:
                output.append(False)
                return
            if right and not left:
                output.append(True)
                return
            isRightOrder(left, right)

        # if left is a list and right is an int
        if type(left) == list and type(right) == int:
            isRightOrder(left, [right])

        # if right is a list and left is an int
        if type(right) == list and type(left) == int:
            isRightOrder([left], right)

        # consider the next item in leftSide and rightSide
        n += 1

    if rightSide and not leftSide:
        output.append(True)


class Pair(object):
    def __init__(self, index, left, right):
        self.index = index
        self.left = left
        self.right = right
    def setIndex(self, index):
        self.index = index
    def getIndex(self):
        return self.index
    def setLeft(self, side):
        self.left = side
    def getLeft(self):
        return self.left
    def setRight(self, side):
        self.right = side
    def getRight(self):
        return self.right
    def __str__(self):
        return 'Pair(' + str(self.getIndex()) + ', left:' + str(self.getLeft()) + ', right:' + str(self.getRight()) + ')'


# create list of pairs
pairs = []
index = 1
for lineIndex in range(len(lines))[::3]:
    pairs.append(Pair(index, eval(lines[lineIndex]), eval(lines[lineIndex + 1])))
    index += 1

# initialize output
correctSum = 0

# check order of each pair, update output with results
for pair in pairs:
    print(pair)
    output = []
    isRightOrder(pair.getLeft(), pair.getRight())
    if not output or output[0]:
        correctSum += pair.getIndex()
        print('above pair is in CORRECT order')
    else:
        print('above pair is in INCORRECT order')
    print('correctSum', correctSum, '\n')

print(correctSum)
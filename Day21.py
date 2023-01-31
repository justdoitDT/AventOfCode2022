# import data
with open('/Users/dthomas/Downloads/input21.txt') as f:
    monkeys = f.readlines()
for index, line in enumerate(monkeys):
    monkeys[index] = line[:-1]
# print(monkeys)



# define Monkey class
class Monkey(object):
    def __init__(self, name, number=None, operation=None, leftMonkey=None, rightMonkey=None):
        self.name = name
        self.number = number
        self.operation = operation
        self.leftMonkey = leftMonkey
        self.rightMonkey = rightMonkey
    def getName(self):
        return self.name
    def setNumber(self):
        if self.getName() == 'humn':
            return
        if self.number:
            return
        elif monkeysDict[self.leftMonkey].getNumber() and monkeysDict[self.rightMonkey].getNumber():
            self.number = eval(str(monkeysDict[self.leftMonkey].getNumber()) + self.operation + str(monkeysDict[self.rightMonkey].getNumber()))
    def getNumber(self):
        return self.number
    def getOperation(self):
        return self.operation
    def getLeftMonkey(self):
        return self.leftMonkey
    def getRightMonkey(self):
        return self.rightMonkey





# Part One

# create hashmap of monkeys
monkeysDict = {}
for monkey in monkeys:
    # if number-yelling monkey
    if monkey[6] in '123456789':
        monkeysDict[monkey[0:4]] = Monkey(monkey[0:4], int(monkey[6:]))
    # if operation monkey
    else:
        monkeysDict[monkey[0:4]] = Monkey(monkey[0:4], None, monkey[11], monkey[6:10], monkey[13:17])


# loop until root monkey has its number
while not monkeysDict['root'].getNumber():
    for monkey in monkeysDict:
        monkeysDict[monkey].setNumber()


print(int(monkeysDict['root'].getNumber()))







# Part Two

import copy

# create hashmap of monkeys
monkeysDict = {}
for monkey in monkeys:
    # if number-yelling monkey
    if monkey[6] in '123456789':
        monkeysDict[monkey[0:4]] = Monkey(monkey[0:4], int(monkey[6:]))
    # if operation monkey
    else:
        monkeysDict[monkey[0:4]] = Monkey(monkey[0:4], None, monkey[11], monkey[6:10], monkey[13:17])
monkeysDict['humn'] = Monkey('humn')
monkeysDictCopy = copy.deepcopy(monkeysDict)


# loop until root's LeftMonkey or RightMonkey has its number
while not (monkeysDict[monkeysDict['root'].getLeftMonkey()].getNumber() or monkeysDict[monkeysDict['root'].getRightMonkey()].getNumber()):
    for monkey in monkeysDict:
        monkeysDict[monkey].setNumber()


# loop some more to complete all monkeys
for _ in range(len(monkeysDict)):
    for monkey in monkeysDict:
        monkeysDict[monkey].setNumber()


# if root's LeftMonkey is shouting a number
if monkeysDict[monkeysDict['root'].getLeftMonkey()].getNumber():
    # set targetNumber to the number root's LeftMonkey is shouting
    targetNumber = monkeysDict[monkeysDict['root'].getLeftMonkey()].getNumber()
    # set currentMonkey to root's RightMonkey
    currentMonkey = monkeysDict['root'].getRightMonkey()
# if root's RightMonkey is shouting a number
else:
    # set targetNumber to the number root's RightMonkey is shouting
    targetNumber = monkeysDict[monkeysDict['root'].getRightMonkey()].getNumber()
    # set currentMonkey to root's LeftMonkey
    currentMonkey = monkeysDict['root'].getLeftMonkey()


# perform inverse operation on targetNumber, loop until reaching 'humn'
while True:
    # stop condition
    if currentMonkey == 'humn':
        print('humn Number:', int(targetNumber))
        break
    # check currentMonkey's left and right monkeys
    leftNumber, rightNumber = monkeysDict[monkeysDict[currentMonkey].leftMonkey].getNumber(), monkeysDict[monkeysDict[currentMonkey].rightMonkey].getNumber()
    # perform inverse operation
    # if multiplication
    if monkeysDict[currentMonkey].getOperation() == '*':
        if leftNumber:
            targetNumber /= leftNumber
            currentMonkey = monkeysDict[currentMonkey].getRightMonkey()
            continue
        else:
            targetNumber /= rightNumber
            currentMonkey = monkeysDict[currentMonkey].getLeftMonkey()
            continue
    # if division
    if monkeysDict[currentMonkey].getOperation() == '/':
        if leftNumber:
            targetNumber *= leftNumber
            currentMonkey = monkeysDict[currentMonkey].getRightMonkey()
            continue
        else:
            targetNumber *= rightNumber
            currentMonkey = monkeysDict[currentMonkey].getLeftMonkey()
            continue
    # if addition
    if monkeysDict[currentMonkey].getOperation() == '+':
        if leftNumber:
            targetNumber -= leftNumber
            currentMonkey = monkeysDict[currentMonkey].getRightMonkey()
            continue
        else:
            targetNumber -= rightNumber
            currentMonkey = monkeysDict[currentMonkey].getLeftMonkey()
            continue
    # if subtraction
    if monkeysDict[currentMonkey].getOperation() == '-':
        if leftNumber:
            targetNumber = leftNumber - targetNumber
            currentMonkey = monkeysDict[currentMonkey].getRightMonkey()
            continue
        else:
            targetNumber = targetNumber + rightNumber
            currentMonkey = monkeysDict[currentMonkey].getLeftMonkey()
            continue


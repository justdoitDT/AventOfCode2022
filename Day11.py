
'''
# Part One

class Monkey(object):
    def __init__(self, inventory, operation, testDivisor, trueTarget=None, falseTarget=None):
        self.inventory = inventory
        self.operation = operation
        self.testDivisor = testDivisor
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.numInspections = 0
    def getInventory(self):
        return self.inventory
    def inspectItem(self):
        self.numInspections += 1
        return self.inventory.pop(0)
    def catchItem(self, item):
        self.inventory.append(item)
    def getOperation(self):
        return self.operation
    def getTestDivisor(self):
        return self.testDivisor
    def setTrueTarget(self, target):
        self.trueTarget = target
    def getTrueTarget(self):
        return self.trueTarget
    def setFalseTarget(self, target):
        self.falseTarget = target
    def getFalseTarget(self):
        return self.falseTarget
    def getNumInspections(self):
        return self.numInspections

# initialize monkeys
monkey0 = Monkey([80], '* 5', 2)
monkey1 = Monkey([75, 83, 74], '+ 7', 7)
monkey2 = Monkey([86, 67, 61, 96, 52, 63, 73], '+ 5', 3)
monkey3 = Monkey([85, 83, 55, 85, 57, 70, 85, 52], '+ 8', 17)
monkey4 = Monkey([67, 75, 91, 72, 89], '+ 4', 11)
monkey5 = Monkey([66, 64, 68, 92, 68, 77], '* 2', 19)
monkey6 = Monkey([97, 94, 79, 88], '* currentItem', 5)
monkey7 = Monkey([77, 85], '+ 6', 13)

# set each monkey's trueTarget and falseTarget
monkey0.setTrueTarget(monkey4)
monkey0.setFalseTarget(monkey3)
monkey1.setTrueTarget(monkey5)
monkey1.setFalseTarget(monkey6)
monkey2.setTrueTarget(monkey7)
monkey2.setFalseTarget(monkey0)
monkey3.setTrueTarget(monkey1)
monkey3.setFalseTarget(monkey5)
monkey4.setTrueTarget(monkey3)
monkey4.setFalseTarget(monkey1)
monkey5.setTrueTarget(monkey6)
monkey5.setFalseTarget(monkey2)
monkey6.setTrueTarget(monkey2)
monkey6.setFalseTarget(monkey7)
monkey7.setTrueTarget(monkey4)
monkey7.setFalseTarget(monkey0)

# create list of monkeys
monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

# execute 20 rounds
for round in range(1, 21):
    # for each monkey
    for monkey in monkeys:
        # for each item monkey is currently holding
        for _ in range(len(monkey.getInventory())):
            # inspect item
            currentItem = monkey.inspectItem()
            # apply monkey's operation
            currentItem = eval('currentItem' + str(monkey.getOperation()))
            # relief
            currentItem //= 3
            # if test is True, throw to trueTarget
            if currentItem % monkey.getTestDivisor() == 0:
                monkey.getTrueTarget().catchItem(currentItem)
            # if test is False, throw to falseTarget
            else:
                monkey.getFalseTarget().catchItem(currentItem)

# calculate and print monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkey.getNumInspections())
inspections.sort()
print(inspections[-1] * inspections[-2])
'''







# Part Two

class Monkey(object):
    def __init__(self, inventory, operation, testDivisor, trueTarget=None, falseTarget=None):
        self.inventory = inventory
        self.operation = operation
        self.testDivisor = testDivisor
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.numInspections = 0
    def getInventory(self):
        return self.inventory
    def inspectItem(self):
        self.numInspections += 1
        return self.inventory.pop(0)
    def catchItem(self, item):
        self.inventory.append(item)
    def getOperation(self):
        return self.operation
    def getTestDivisor(self):
        return self.testDivisor
    def setTrueTarget(self, target):
        self.trueTarget = target
    def getTrueTarget(self):
        return self.trueTarget
    def setFalseTarget(self, target):
        self.falseTarget = target
    def getFalseTarget(self):
        return self.falseTarget
    def getNumInspections(self):
        return self.numInspections

# initialize monkeys
monkey0 = Monkey([80], '* 5', 2)
monkey1 = Monkey([75, 83, 74], '+ 7', 7)
monkey2 = Monkey([86, 67, 61, 96, 52, 63, 73], '+ 5', 3)
monkey3 = Monkey([85, 83, 55, 85, 57, 70, 85, 52], '+ 8', 17)
monkey4 = Monkey([67, 75, 91, 72, 89], '+ 4', 11)
monkey5 = Monkey([66, 64, 68, 92, 68, 77], '* 2', 19)
monkey6 = Monkey([97, 94, 79, 88], '* currentItem', 5)
monkey7 = Monkey([77, 85], '+ 6', 13)

# set each monkey's trueTarget and falseTarget
monkey0.setTrueTarget(monkey4)
monkey0.setFalseTarget(monkey3)
monkey1.setTrueTarget(monkey5)
monkey1.setFalseTarget(monkey6)
monkey2.setTrueTarget(monkey7)
monkey2.setFalseTarget(monkey0)
monkey3.setTrueTarget(monkey1)
monkey3.setFalseTarget(monkey5)
monkey4.setTrueTarget(monkey3)
monkey4.setFalseTarget(monkey1)
monkey5.setTrueTarget(monkey6)
monkey5.setFalseTarget(monkey2)
monkey6.setTrueTarget(monkey2)
monkey6.setFalseTarget(monkey7)
monkey7.setTrueTarget(monkey4)
monkey7.setFalseTarget(monkey0)

# create list of monkeys
monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

# execute 10,000 rounds
for round in range(1, 10001):
    print(round)
    # for each monkey
    for monkey in monkeys:
        # for each item monkey is currently holding
        while monkey.getInventory():
            # inspect item
            currentItem = monkey.inspectItem()
            # apply monkey's operation
            currentItem = eval('currentItem' + str(monkey.getOperation()))
            # manage worry
            currentItem %= 9699690
            # if test is True, throw to trueTarget
            if currentItem % monkey.getTestDivisor() == 0:
                monkey.getTrueTarget().catchItem(currentItem)
            # if test is False, throw to falseTarget
            else:
                monkey.getFalseTarget().catchItem(currentItem)

# calculate and print monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkey.getNumInspections())
inspections.sort()
print(inspections[-1] * inspections[-2])






'''
# simpler attempt at Part Two

# initialize monkeys
monkey0 = [80]
monkey1 = [75, 83, 74]
monkey2 = [86, 67, 61, 96, 52, 63, 73]
monkey3 = [85, 83, 55, 85, 57, 70, 85, 52]
monkey4 = [67, 75, 91, 72, 89]
monkey5 = [66, 64, 68, 92, 68, 77]
monkey6 = [97, 94, 79, 88]
monkey7 = [77, 85]

# initialize inspections
inspections = [0, 0, 0, 0, 0, 0, 0, 0]

# execute 10,000 rounds
for round in range(1, 10001):
    print(round)
    # monkey 0
    while monkey0:
        inspections[0] += 1
        currentItem = monkey0.pop(0)
        currentItem = currentItem * 5
        if currentItem % 2 == 0:
            monkey4.append(currentItem)
        else:
            monkey3.append(currentItem)
    # monkey 1
    while monkey1:
        inspections[1] += 1
        currentItem = monkey1.pop(0)
        currentItem = currentItem + 7
        if currentItem % 7 == 0:
            monkey5.append(currentItem)
        else:
            monkey6.append(currentItem)
    # monkey 2
    while monkey2:
        inspections[2] += 1
        currentItem = monkey2.pop(0)
        currentItem = currentItem + 5
        if currentItem % 3 == 0:
            monkey7.append(currentItem)
        else:
            monkey0.append(currentItem)
    # monkey 3
    while monkey3:
        inspections[3] += 1
        currentItem = monkey3.pop(0)
        currentItem = currentItem + 8
        if currentItem % 17 == 0:
            monkey1.append(currentItem)
        else:
            monkey5.append(currentItem)
    # monkey 4
    while monkey4:
        inspections[4] += 1
        currentItem = monkey4.pop(0)
        currentItem = currentItem + 4
        if currentItem % 11 == 0:
            monkey3.append(currentItem)
        else:
            monkey1.append(currentItem)
    # monkey 5
    while monkey5:
        inspections[5] += 1
        currentItem = monkey5.pop(0)
        currentItem = currentItem * 2
        if currentItem % 19 == 0:
            monkey6.append(currentItem)
        else:
            monkey2.append(currentItem)
    # monkey 6
    while monkey6:
        inspections[6] += 1
        currentItem = monkey6.pop(0)
        currentItem = currentItem * currentItem
        if currentItem % 5 == 0:
            monkey2.append(currentItem)
        else:
            monkey7.append(currentItem)
    # monkey 7
    while monkey7:
        inspections[7] += 1
        currentItem = monkey7.pop(0)
        currentItem = currentItem + 6
        if currentItem % 13 == 0:
            monkey4.append(currentItem)
        else:
            monkey0.append(currentItem)

inspections.sort()
print(inspections[-1] * inspections[-2])
'''
with open('/Users/dthomas/Downloads/input10.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
# print(lines)



'''
# Part One

currentCycle = 1
X = 1
checkCycles = {20, 60, 100, 140, 180, 220}
signalStrengths = []

for line in lines:
    # if no operation
    if line == 'noop':
        # check
        if currentCycle in checkCycles:
            signalStrengths.append(currentCycle * X)
        # advance
        currentCycle += 1

    # if addx operation
    else:
        # check
        if currentCycle in checkCycles:
            signalStrengths.append(currentCycle * X)
        # advance
        currentCycle += 1
        # check
        if currentCycle in checkCycles:
            signalStrengths.append(currentCycle * X)
        # advance
        currentCycle += 1
        # complete addx execution
        X += int(line[5:])

print(sum(signalStrengths))
'''



# Part Two

CRT = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]


def drawPixel(sprite, currentCycle):
    if sprite <= currentCycle % 40 <= sprite + 2:
        CRT[currentCycle // 40][currentCycle % 40] = '#'
    else:
        CRT[currentCycle // 40][currentCycle % 40] = '.'


currentCycle = 0
sprite = 0

for line in lines:
    # if no operation
    if line == 'noop':
        # draw pixel
        drawPixel(sprite, currentCycle)
        # advance cycle
        currentCycle += 1

    # if addx operation
    else:
        # draw pixel
        drawPixel(sprite, currentCycle)
        # advance cycle
        currentCycle += 1
        # draw pixel
        drawPixel(sprite, currentCycle)
        # advance cycle
        currentCycle += 1
        # complete addx execution
        sprite += int(line[5:])


for line in CRT:
    print(line)
import copy

with open('/Users/dthomas/Downloads/input5.txt') as f:
    lines = f.readlines()

lines = lines[10:]
print(lines)

# Part One

stacks = ['placeholder',['R','N','F','V','L','J','S','M'],['P','N','D','Z','F','J','W','H'],['W','R','C','D','G'],['N','B','S'],['M','Z','W','P','C','B','F','N'],['P','R','M','W'],['R','T','N','G','L','S','W'],['Q','T','H','F','N','B','V'],['L','M','H','Z','N','F']]
originalStacks = copy.deepcopy(stacks)

for stack in stacks:
    print(stack)

for line in lines:
    print('\n')
    print(line)
    # single-digit moves
    if line[6] == ' ':
        for _ in range(int(line[5])):
            # if stack not empty, move crate
            if stacks[int(line[12])]:
                stacks[int(line[17])].append(stacks[int(line[12])].pop())
    # double-digit moves
    else:
        for _ in range(int(line[5:7])):
            # if stack not empty, move crate
            if stacks[int(line[13])]:
                stacks[int(line[18])].append(stacks[int(line[13])].pop())
    for stack in stacks:
        print(stack)

topCrates = ''
for stack in stacks[1:]:
    if stack:
        topCrates += stack[-1]

print(topCrates)


# Part Two

stacks = originalStacks
temp = []

for line in lines:
    # single-digit moves
    if line[6] == ' ':
        for _ in range(int(line[5])):
            # if stack not empty, move crate
            if stacks[int(line[12])]:
                temp.append(stacks[int(line[12])].pop())
        while temp:
            stacks[int(line[17])].append(temp.pop())
    # double-digit moves
    else:
        for _ in range(int(line[5:7])):
            # if stack not empty, move crate
            if stacks[int(line[13])]:
                temp.append(stacks[int(line[13])].pop())
        while temp:
            stacks[int(line[18])].append(temp.pop())
    for stack in stacks:
        print(stack)

topCrates = ''
for stack in stacks[1:]:
    if stack:
        topCrates += stack[-1]

print(topCrates)
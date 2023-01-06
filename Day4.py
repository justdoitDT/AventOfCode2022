with open('/Users/dthomas/Downloads/input4.txt') as f:
    lines = f.readlines()

print(lines)

for index, line in enumerate(lines):
    lines[index] = line[:-1]

print(lines)

total = 0
pairs = []

for line in lines:
    line = line.split(',')
    pairs.append((line[0].split('-'), line[1].split('-')))

print(pairs)

for pair in pairs:
    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
        total += 1
    elif int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1]):
        total += 1

print('lenPairs', len(pairs))
print(total)


# Part Two

total = 0

for pair in pairs:
    elf1 = [int(pair[0][0]), int(pair[0][1])]
    elf2 = [int(pair[1][0]), int(pair[1][1])]
    if elf2[0] <= elf1[0] <= elf2[1] or elf1[0] <= elf2[0] <= elf1[1] or elf2[0] <= elf1[1] <= elf2[1] or elf1[0] <= elf2[1] <= elf1[1]:
        total += 1

print(total)
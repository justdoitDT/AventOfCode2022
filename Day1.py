with open('/Users/dthomas/Downloads/input.txt') as f:
    lines = f.readlines()

#Day 1: Part 1

totals = [0]
elf = 0

for i in lines:
    if i == '\n':
        totals.append(0)
        elf += 1
    else:
        totals[elf] += int(i[:-1])

print(max(totals))

# Day 1: Part 2

totals.sort()

print(totals[::-1][:3])
print(sum(totals[::-1][:3]))
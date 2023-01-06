with open('/Users/dthomas/Downloads/input6.txt') as f:
    lines = f.readlines()

data = lines[0][:-1]


# Part One

pointer = 4

while len(set(data[pointer-4 : pointer])) < 4:
    pointer += 1

print(pointer)



# Part Two

pointer = 14

while len(set(data[pointer-14 : pointer])) < 14:
    pointer += 1

print(pointer)
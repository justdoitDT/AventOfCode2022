with open('/Users/dthomas/Downloads/input3.txt') as f:
    lines = f.readlines()

print(lines)


# Part One

for index, line in enumerate(lines):
    lines[index] = line[:-1]

print(lines)

total = 0

prioritiesDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

for line in lines:
    compartment1 = set(line[:len(line)//2])
    compartment2 = set(line[len(line)//2:])
    for item in compartment1:
        if item in compartment2:
            total += prioritiesDict[item]
            break

print(total)


# Part Two
total = 0
pointer = 0
lenLines = len(lines)
while pointer < len(lines):
    elf1 = set(lines[pointer])
    elf2 = set(lines[pointer + 1])
    elf3 = set(lines[pointer + 2])
    for item in elf1:
        if item in elf2 and item in elf3:
            total += prioritiesDict[item]
            break
    pointer += 3

print(total)
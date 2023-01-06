with open('/Users/dthomas/Downloads/input2.txt') as f:
    lines = f.readlines()

print(lines)


# Part One

total = 0

for i in lines:
    # you play rock
    if i[2] == 'X':
        print('you play rock')
        total += 1
        print('1 point for rock. total = ', total)
        # opponent plays rock
        print('opponent plays rock')
        if i[0] == 'A':
            total += 3
            print('tie. total = ', total)
        # opponent plays paper
        print('opponent plays paper')
        if i[0] == 'B':
            total += 0
            print('loss. total = ', total)
        # opponent plays scissors
        print('opponent plays scissors')
        if i[0] == 'C':
            total += 6
            print('win. total = ', total)
    # you play paper
    if i[2] == 'Y':
        print('you play paper')
        total += 2
        print('2 points for paper. total = ', total)
        # opponent plays rock
        print('opponent plays rock')
        if i[0] == 'A':
            total += 6
            print('win. total = ', total)
        # opponent plays paper
        print('opponent plays paper')
        if i[0] == 'B':
            total += 3
            print('tie. total = ', total)
        # opponent plays scissors
        print('opponent plays scissors')
        if i[0] == 'C':
            total += 0
            print('loss. total = ', total)
    # you play scissors
    if i[2] == 'Z':
        print('you play scissors')
        total += 3
        print('3 points for scissors. total = ', total)
        # opponent plays rock
        print('opponent plays rock')
        if i[0] == 'A':
            total += 0
            print('loss. total = ', total)
        # opponent plays paper
        print('opponent plays paper')
        if i[0] == 'B':
            total += 6
            print('win. total = ', total)
        # opponent plays scissors
        print('opponent plays scissors')
        if i[0] == 'C':
            total += 3
            print('tie. total = ', total)

print(total)

# Part Two

total = 0

for i in lines:

    # if opponent plays rock
    if i[0] == 'A':
        # if you must lose, you play scissors
        if i[2] == 'X':
            total += 3  # 3 for scissors, 0 for loss
        # if you must tie, you play rock
        if i[2] == 'Y':
            total += 4 # 1 for rock, 3 for tie
        # if you must win, you play paper
        if i[2] == 'Z':
            total += 8 # 2 for paper, 6 for win

    # if opponent plays paper
    if i[0] == 'B':
        # if you must lose, you play rock
        if i[2] == 'X':
            total += 1  # 1 for rock, 0 for loss
        # if you must tie, you play paper
        if i[2] == 'Y':
            total += 5 # 2 for paper, 3 for tie
        # if you must win, you play scissors
        if i[2] == 'Z':
            total += 9 # 3 for scissors, 6 for win

    # if opponent plays scissors
    if i[0] == 'C':
        # if you must lose, you play paper
        if i[2] == 'X':
            total += 2  # 2 for paper, 0 for loss
        # if you must tie, you play scissors
        if i[2] == 'Y':
            total += 6 # 3 for scissors, 3 for tie
        # if you must win, you play rock
        if i[2] == 'Z':
            total += 7 # 1 for rock, 6 for win

print(total)
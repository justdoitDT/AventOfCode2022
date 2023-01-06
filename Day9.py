with open('/Users/dthomas/Downloads/input9.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
# print(lines)


# Part One
'''
head = [0, 0]    # [row, col]
tail = [0, 0]    # [row, col]
visited = {(0, 0)}

# execute motions
for line in lines:
    # for each step
    for _ in range(int(line[2:])):
        # move head
        if line[0] == 'U':
            head[0] += -1
        if line[0] == 'D':
            head[0] += 1
        if line[0] == 'L':
            head[1] += -1
        if line[0] == 'R':
            head[1] += 1
        # move tail if not touching head
        # if tail above head by 2 rows
        if head[0] - tail[0] == 2:
            tail[0] += 1
            tail[1] += head[1] - tail[1]
        # if tail below head by 2 rows
        if head[0] - tail[0] == -2:
            tail[0] += -1
            tail[1] += head[1] - tail[1]
        # if tail left of head by 2 cols
        if head[1] - tail[1] == 2:
            tail[1] += 1
            tail[0] += head[0] - tail[0]
        # if tail right of head by 2 cols
        if head[1] - tail[1] == -2:
            tail[1] += -1
            tail[0] += head[0] - tail[0]
        # add tail's new position to visited
        visited.add(tuple(tail))

print(len(visited))
'''





# Part Two

def moveKnot(leadKnot, trailKnot):
    # move trailKnot if not touching leadKnot
    # if trailKnot above leadKnot by 2 rows
    if leadKnot[0] - trailKnot[0] == 2:
        trailKnot[0] += 1
        # if trailKnot also left or right by 2 cols
        if abs(leadKnot[1] - trailKnot[1]) == 2:
            trailKnot[1] += (leadKnot[1] - trailKnot[1])//2
        # if trailKnot only left or right by 0 or 1 cols
        else:
            trailKnot[1] += leadKnot[1] - trailKnot[1]
    # if tail below head by 2 rows
    if leadKnot[0] - trailKnot[0] == -2:
        trailKnot[0] += -1
        # if trailKnot also left or right by 2 cols
        if abs(leadKnot[1] - trailKnot[1]) == 2:
            trailKnot[1] += (leadKnot[1] - trailKnot[1])//2
        # if trailKnot only left or right by 0 or 1 cols
        else:
            trailKnot[1] += leadKnot[1] - trailKnot[1]
    # if tail left of head by 2 cols
    if leadKnot[1] - trailKnot[1] == 2:
        trailKnot[1] += 1
        # if trailKnot also above or below by 2 rows
        if abs(leadKnot[0] - trailKnot[0]) == 2:
            trailKnot[0] += (leadKnot[0] - trailKnot[0])//2
        # if trailKnot only above or below by 0 or 1 rows
        else:
            trailKnot[0] += leadKnot[0] - trailKnot[0]
    # if tail right of head by 2 cols
    if leadKnot[1] - trailKnot[1] == -2:
        trailKnot[1] += -1
        # if trailKnot also above or below by 2 rows
        if abs(leadKnot[0] - trailKnot[0]) == 2:
            trailKnot[0] += (leadKnot[0] - trailKnot[0])//2
        # if trailKnot only above or below by 0 or 1 rows
        else:
            trailKnot[0] += leadKnot[0] - trailKnot[0]
    return trailKnot

# initialize all knots at (0, 0)
head = [0, 0]
knot1 = [0, 0]
knot2 = [0, 0]
knot3 = [0, 0]
knot4 = [0, 0]
knot5 = [0, 0]
knot6 = [0, 0]
knot7 = [0, 0]
knot8 = [0, 0]
tail = [0, 0]
visited = {(0, 0)}

# execute motions
for line in lines:
    # for each step in line
    for _ in range(int(line[2:])):
        # move head
        if line[0] == 'U':
            head[0] += -1
        if line[0] == 'D':
            head[0] += 1
        if line[0] == 'L':
            head[1] += -1
        if line[0] == 'R':
            head[1] += 1
        # move the other 9 knots if necessary
        knot1 = moveKnot(head, knot1)
        knot2 = moveKnot(knot1, knot2)
        knot3 = moveKnot(knot2, knot3)
        knot4 = moveKnot(knot3, knot4)
        knot5 = moveKnot(knot4, knot5)
        knot6 = moveKnot(knot5, knot6)
        knot7 = moveKnot(knot6, knot7)
        knot8 = moveKnot(knot7, knot8)
        tail = moveKnot(knot8, tail)
        # add tail's new position to visited
        visited.add(tuple(tail))
        # print(line, _)
        # print('head', head)
        # print('knot1', knot1)
        # print('knot2', knot2)
        # print('knot3', knot3)
        # print('knot4', knot4)
        # print('knot5', knot5)
        # print('knot6', knot6)
        # print('knot7', knot7)
        # print('knot8', knot8)
        # print('tail', tail)

print(len(visited))



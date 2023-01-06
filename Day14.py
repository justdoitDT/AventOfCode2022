# import data set
with open('/Users/dthomas/Downloads/input14.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]
paths = []

# create list of coordinates in each path
for line in lines:
    paths.append(line.split(' -> '))
    currentPath = paths[-1]
    paths[-1] = []
    for segment in currentPath:
        paths[-1].append(segment.split(','))
        for index, coord in enumerate(paths[-1]):
            paths[-1][index] = (int(coord[0]), int(coord[1]))

# initialize set of all blocked coordinates
blocked = set([])

# in each path, add all coordinates between successive coordinates to blocked
for path in paths:
    for index in range(len(path) - 1):
    # if x1 = x2, add vertical segment
        if path[index][0] == path[index + 1][0]:
        # add coordinates from (x1, ymin) to (x1, ymax)
            for num in range(min(path[index][1], path[index + 1][1]), max(path[index][1], path[index + 1][1]) + 1):
                blocked.add((path[index][0], num))
        # if y1 = y2, add horizontal segment
        if path[index][1] == path[index + 1][1]:
            # add coordinates from (xmin, y1) to (xmax, y1)
            for num in range(min(path[index][0], path[index + 1][0]), max(path[index][0], path[index + 1][0]) + 1):
                blocked.add((num, path[index][1]))

# create a copy of blocked for use in Part Two
blockedCopy = blocked.copy()

# determine depth of lowest rock
ymax = -float('inf')
for path in paths:
    for coord in path:
        if coord[1] > ymax:
            ymax = coord[1]



# Part One

# drop sand until a sand gets lower than the lowest rock
totalSand = 0
# until a sand gets lower than ymax
flag = True
while flag:
    current = (500, 0)
    totalSand += 1
    # until sand comes to rest
    while True:
        # check if sand reaches abyss
        if current[1] > ymax:
            flag = False
            break
        # try to move sand down
        if (current[0], current[1] + 1) not in blocked:
            current = (current[0], current[1] + 1)
            continue
        # try to move sand down-left
        if (current[0] - 1, current[1] + 1) not in blocked:
            current = (current[0] - 1, current[1] + 1)
            continue
        # try to move sand down right
        if (current[0] + 1, current[1] + 1) not in blocked:
            current = (current[0] + 1, current[1] + 1)
            continue
        # sand is now at rest
        blocked.add(current)
        break

print(totalSand - 1)




# Part Two

# reset blocked from before Part One
blocked = blockedCopy

# add floor
for col in range(-10000, 10000):
    blocked.add((col, 183))

# initialize totalSand count
totalSand = 0

# drop sand until (500, 0) is blocked
flag = True
while flag:
    current = (500, 0)
    totalSand += 1
    # until sand comes to rest
    while True:
        # check if (500, 0) is blocked
        if (500, 0) in blocked:
            flag = False
            break
        # try to move sand down
        if (current[0], current[1] + 1) not in blocked:
            current = (current[0], current[1] + 1)
            continue
        # try to move sand down-left
        if (current[0] - 1, current[1] + 1) not in blocked:
            current = (current[0] - 1, current[1] + 1)
            continue
        # try to move sand down right
        if (current[0] + 1, current[1] + 1) not in blocked:
            current = (current[0] + 1, current[1] + 1)
            continue
        # sand is now at rest
        blocked.add(current)
        break

print(totalSand - 1)
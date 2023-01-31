# import data set
with open('/Users/dthomas/Downloads/input18.txt') as f:
    cubes = f.readlines()
for index, line in enumerate(cubes):
    cubes[index] = line[:-1]
for index in range(len(cubes)):
    cubes[index] = cubes[index].split(',')
for index, [x, y, z] in enumerate(cubes):
    cubes[index] = [int(x), int(y), int(z)]
# print(lines)

# create set of coordinates of all cubes
cubesSet = set([])
for x, y, z in cubes:
    cubesSet.add((x, y, z))




# Part One

# initialize surface area assuming no adjacent cubes
surfaceArea = 6 * len(cubes)

# subtract 1 from surface area for each adjacent cube
for x, y, z in cubes:
    if (x + 1, y, z) in cubesSet:
        surfaceArea -= 1
    if (x - 1, y, z) in cubesSet:
        surfaceArea -= 1
    if (x, y + 1, z) in cubesSet:
        surfaceArea -= 1
    if (x, y - 1, z) in cubesSet:
        surfaceArea -= 1
    if (x, y, z + 1) in cubesSet:
        surfaceArea -= 1
    if (x, y, z - 1) in cubesSet:
        surfaceArea -= 1

print(surfaceArea)






# Part Two

# find constraints of rectangular box containing lava
xmin = float('inf')
ymin = float('inf')
zmin = float('inf')
xmax = -float('inf')
ymax = -float('inf')
zmax = -float('inf')
for x, y, z in cubes:
    if x < xmin:
        xmin = x
    if y < ymin:
        ymin = y
    if z < zmin:
        zmin = z
    if x > xmax:
        xmax = x
    if y > ymax:
        ymax = y
    if z > zmax:
        zmax = z


# find all external air. pick an air coordinate, breadth-first search for all other air touching it
extAir = set([])
queue = [(xmin - 1, ymin - 1, zmin - 1)]
directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
while queue:
    x, y, z = queue.pop(0)
    # check each neighboring coordinate
    for xdir, ydir, zdir in directions:
        # if neighbor coordinate is inside rectangular box, is not lava, and is not already accounted for
        if x + xdir > xmin - 2 and x + xdir < xmax + 2 \
                and y + ydir > ymin - 2 and y + ydir < ymax + 2 \
                and z + zdir > zmin - 2 and z + zdir < zmax + 2 \
                and (x + xdir, y + ydir, z + zdir) not in cubesSet \
                and (x + xdir, y + ydir, z + zdir) not in extAir:
            # add neighbor coordinate to set of external air
            extAir.add((x + xdir, y + ydir, z + zdir))
            # append neighbor coordinate to the queue
            queue.append((x + xdir, y + ydir, z + zdir))


# for each external air coordinate, count the number of adjacent lava coordinates
surfaceArea = 0
for x, y, z in extAir:
    # check each neighboring coordinate
    for xdir, ydir, zdir in directions:
        if (x + xdir, y + ydir, z + zdir) in cubesSet:
            surfaceArea += 1

print(surfaceArea)

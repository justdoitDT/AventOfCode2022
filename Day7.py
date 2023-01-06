with open('/Users/dthomas/Downloads/input7.txt') as f:
    lines = f.readlines()
for index, line in enumerate(lines):
    lines[index] = line[:-1]


class File(object):
    def __init__(self, sizeName):
        self.size = int(sizeName.split(' ')[0])
        self.name = sizeName.split(' ')[1]
    def getSize(self):
        return self.size
    def getName(self):
        return self.name


class Directory(object):
    def __init__(self, name, superDirectory):
        self.name = name
        self.superDirectory = superDirectory
        self.files = []
        self.subDirectoriesDict = {}
    def getName(self):
        return self.name
    def getSuperDirectory(self):
        return self.superDirectory
    def addFile(self, file):
        self.files.append(file)
    def getFiles(self):
        return self.files
    def addSubDirectory(self, subDirectory):
        self.subDirectoriesDict[subDirectory] = Directory(subDirectory, self)
    def getSubDirectoriesDict(self):
        return self.subDirectoriesDict
    def getSubDirectoriesList(self):
        return list(self.subDirectoriesDict.values())
    def setSize(self):
        self.size = 0
        for file in self.getFiles():
            self.size += file.getSize()
        for subDirectory in self.getSubDirectoriesList():
            self.size += subDirectory.getSize()
    def getSize(self):
        return self.size


# initialize root directory, point to it
root = Directory('/', None)
currentDirectory = root


# iterate through puzzle input, build data structure
for line in lines:
    # if current line is a command
    if line[0] == '$':
        # if change directory command
        if line[2:4] == 'cd':
            # if move out command
            if line[5:] == '..':
                # change currentDirectory to currentDirectory's superDirectory
                currentDirectory = currentDirectory.getSuperDirectory()
            # if move to root
            elif line[5:] == '/':
                # do nothing
                pass
            # if specific cd command
            else:
                # change currentDirectory to specified directory
                currentDirectory = currentDirectory.getSubDirectoriesDict()[line[5:]]
        # if list command
            # do nothing
    # if current line is a file
    elif line[0] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        currentDirectory.addFile(File(line))
    # if current line is a directory
    else:
        # add new directory to currentDirectory's subDirectoriesDict
        currentDirectory.addSubDirectory(line[4:])





# Part One
'''
# initialize list of qualified directory sizes to be summed
qualifiedSizes = []

# run a depth-first search through data structure for all qualifying directories
def dfs(directory):
    for subDirectory in directory.getSubDirectoriesList():
        dfs(subDirectory)
    # after searching all subDirectories, calculate the directory's size
    directory.setSize()
    # if it qualifies, include directory's size in list to be summed
    if 0 < directory.getSize() <= 100000:
        qualifiedSizes.append(directory.getSize())
    return

dfs(root)
print(sum(qualifiedSizes))
'''





# Part Two

# initialize list of qualified directory sizes
qualifiedSizes = []

# run a depth-first search through data structure to measure and set sizes for all directories
def dfsSetSizes(directory):
    for subDirectory in directory.getSubDirectoriesList():
        dfsSetSizes(subDirectory)
    # after searching all subDirectories, calculate the directory's size
    directory.setSize()

dfsSetSizes(root)


# run a depth-first search to find qualifying directories
def dfsFindQualified(directory):
    for subDirectory in directory.getSubDirectoriesList():
        dfsFindQualified(subDirectory)
    # if it qualifies, include directory's size in list
    if directory.getSize() >= root.getSize() - 40000000:
        qualifiedSizes.append(directory.getSize())
    return

dfsFindQualified(root)
print(min(qualifiedSizes))






# print data structure
def dfsPrint(directory, depth):
    print('   ' * depth, directory.getName(), '(dir, size='+str(directory.getSize())+')')
    for file in directory.getFiles():
        print('   ' * (depth + 1), file.getName(), '(file, size='+str(file.getSize())+')')
    for subDirectory in directory.getSubDirectoriesList():
        dfsPrint(subDirectory, depth + 1)

# dfsPrint(root, 0)


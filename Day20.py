# import data set
with open('/Users/dthomas/Downloads/input20.txt') as f:
    data = f.readlines()
for index, line in enumerate(data):
    data[index] = int(line[:-1])




# Linked list solution, not sure why it doesn't work. Works on all test sets I've tried, but not on given data set.
# Part One


# # debugging
# data = [1, 2, -3, 3, -2, 0, 4]
# def printLinkedList(head, lenData):
#     outputList = []
#     for _ in range(lenData):
#         outputList.append(head.value)
#         head = head.next
#     return outputList


# memoize length of data set
lenData = len(data)


# turn data into a linked list
# define ListNode class
class ListNode(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# create a hashmap of ListNodes and link them together
nodesDict = {}
# create first node
head = ListNode(data[0])
# add first node to nodesDict
nodesDict[0] = head
# prepare to iterate through data set
previous = head
# iterate through data set
for index in range(1, lenData):
    # create new node
    current = ListNode(data[index])
    # add new node to nodesDict
    nodesDict[index] = current
    # link previous and current nodes
    previous.next = current
    current.prev = previous
    # advance to next node
    previous = current

# loop the linked list
current.next = head
head.prev = current

# move each node according to its value
for index in range(lenData):
    # move pointer to next node in order of original data set
    pointer = nodesDict[index]
    # set moveBy based on value of data point
    moveBy = pointer.value
    # do nothing if node would be put back in the same place
    if moveBy % lenData == 0:
        # remember which node is the zeroNode for later
        if moveBy == 0:
            zeroNode = nodesDict[index]
        continue
    # otherwise, modulate moveBy so that it's positive and between 0 and lenData
    elif moveBy > 0:
        moveBy %= lenData
    elif moveBy < 0:
        moveBy %= -lenData
        moveBy += lenData - 1
    # patch hole left by removed node
    nodesDict[index].prev.next = nodesDict[index].next
    nodesDict[index].next.prev = nodesDict[index].prev
    # advance pointer to target location
    for _ in range(moveBy):
        pointer = pointer.next
    # place node in its new location
    nodesDict[index].next = pointer.next
    pointer.next.prev = nodesDict[index]
    pointer.next = nodesDict[index]
    nodesDict[index].prev = pointer
    # print('index:', index, 'number:', nodesDict[index].value, ' moveBy:', moveBy, printLinkedList(head, lenData))


# locate and sum grove coordinates
coordinateSum = 0
current = zeroNode
for _ in range(3):
    for __ in range(1000):
        current = current.next
    coordinateSum += current.value
print(coordinateSum)


# import data
with open('/Users/dthomas/Downloads/input25.txt') as f:
    fuelReqs = f.readlines()
for index, line in enumerate(fuelReqs):
    fuelReqs[index] = line[:-1]


# define function to convert from SNAFU to ordinary base-10 number
def fromSNAFU(SNAFU):
    # define values of each character
    valuesDict = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
    # memoize length of input SNAFU
    lenSNAFU = len(SNAFU)
    # initialize output
    output = 0
    # iterate through each decimal place
    for i in range(lenSNAFU):
        index = lenSNAFU - 1 - i
        output += valuesDict[SNAFU[index]] * 5**i
    # return output
    return output


def fromBaseTen(inputNum):

    # first, convert inputNum to base-5
    # determine smallest power of 5 larger than inputNum
    maxPower = 0
    while 5**maxPower < inputNum:
        maxPower += 1
    maxPower -= 1
    # set up list of lists to contain each digit
    baseFive = []
    for index in range(maxPower + 1):
        baseFive.append(inputNum // 5**(maxPower - index))
        inputNum %= 5**(maxPower - index)

    # add potential digit out front
    baseFive = [0] + baseFive

    # fix all 3's and 4's
    for index in range(1, len(baseFive)):
        # check for 3 or 4
        if baseFive[index] == 3 or baseFive[index] == 4:
            # add one to next highest place
            baseFive[index - 1] += 1
            # reduce current place
            baseFive[index] -= 5

    # initialize output
    SNAFU = ''

    # convert modified baseFive list to SNAFU
    for digit in baseFive:
        if digit == 2:
            SNAFU += '2'
        elif digit == 1:
            SNAFU += '1'
        elif digit == 0:
            SNAFU += '0'
        elif digit == -1:
            SNAFU += '-'
        elif digit == -2:
            SNAFU += '='

    # return SNAFU
    # cut off initial 0 if it starts with 0
    if SNAFU[0] == '0':
        return SNAFU[1:]
    return SNAFU



# initialize sum
sum = 0
for fuelReq in fuelReqs:
    sum += fromSNAFU(fuelReq)


# convert sum to SNAFU
print(fromBaseTen(sum))
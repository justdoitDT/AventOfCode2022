import re

# import data
with open('/Users/dthomas/Downloads/input19.txt') as f:
    blueprints = f.readlines()
for index, line in enumerate(blueprints):
    blueprints[index] = line[:-1]
for index in range(len(blueprints)):
    blueprints[index] = re.split(r'Blueprint |: Each ore robot costs | ore. Each clay robot costs | ore. Each obsidian robot costs | ore and | clay. Each geode robot costs | obsidian.', blueprints[index])[1:-1]
# print(blueprints)




# Part One


# doesn't find the optimal solutions
'''
qualityLevels = []

for blueprint in blueprints:
    blueprintID = int(blueprint[0])
    print('\n', blueprintID, '\n')
    oreBotCost = [int(blueprint[1])]
    clayBotCost = [int(blueprint[2])]
    obsidianBotCost = [int(blueprint[3]), int(blueprint[4])]   # [ore, clay]
    geodeBotCost = [int(blueprint[5]), int(blueprint[6])]   # [ore, obsidian]

    maxGeodes = [0]

    # depth first search, build geodeBots as early as possible
    def dfs(elapsedTime, ore, clay, obsidian, geodes, oreBots, clayBots, obsidianBots, geodeBots):
        print('elapsedTime:', elapsedTime, ' ore:', ore, ' clay:', clay, ' obsidian:', obsidian, ' geodes:', geodes, ' oreBots:', oreBots, ' clayBots:', clayBots, ' obsidianBots:', obsidianBots, ' geodeBots:', geodeBots)
        # stop condition
        if elapsedTime == 24:
            if geodes > maxGeodes[0]:
                maxGeodes[0] = geodes
            return

        # build as many geodeBots as possible
        geodeBotsBuilt = 0
        while ore >= geodeBotCost[0] and obsidian >= geodeBotCost[1]:
            geodeBotsBuilt += 1
            ore -= geodeBotCost[0]
            obsidian -= geodeBotCost[1]

        # build as many obsidianBots as possible
        obsidianBotsBuilt = 0
        while ore >= obsidianBotCost[0] and clay >= obsidianBotCost[1]:
            obsidianBotsBuilt += 1
            ore -= obsidianBotCost[0]
            clay -= obsidianBotCost[1]

        # build as many clayBots as possible
        clayBotsBuilt = 0
        while ore >= clayBotCost[0]:
            clayBotsBuilt += 1
            ore -= clayBotCost[0]

        # build as many oreBots as possible
        oreBotsBuilt = 0
        while ore >= oreBotCost[0]:
            oreBotsBuilt += 1
            ore -= oreBotCost[0]

        dfs(elapsedTime + 1, ore + oreBots, clay + clayBots, obsidian + obsidianBots, geodes + geodeBots, oreBots + oreBotsBuilt, clayBots + clayBotsBuilt, obsidianBots + obsidianBotsBuilt, geodeBots + geodeBotsBuilt)
        return
'''


    # DFS trying every choice takes too long
    '''
    # depth first search, try every possible choice
    def dfs(elapsedTime, ore, clay, obsidian, geodes, oreBots, clayBots, obsidianBots, geodeBots):
        # print('elapsedTime', elapsedTime, 'ore', ore, 'clay', clay, 'obsidian', obsidian, 'geodes', geodes, 'oreBots', oreBots, 'clayBots', clayBots, 'obsidianBots', obsidianBots, 'geodeBots', geodeBots)
        # stop condition
        if elapsedTime == 24:
            if geodes > maxGeodes[0]:
                maxGeodes[0] = geodes
            return
        # # try building nothing
        # dfs(elapsedTime + 1, ore + oreBots, clay + clayBots, obsidian + obsidianBots, geodes + geodeBots, oreBots, clayBots, obsidianBots, geodeBots)
        # try every combination of affordable builds
        for buildOreBots in range(ore//oreBotCost[0] + 1):
            for buildClayBots in range(ore//clayBotCost[0] + 1):
                for buildObsidianBots in range(min(ore//obsidianBotCost[0], clay//obsidianBotCost[1]) + 1):
                    for buildGeodeBots in range(min(ore//geodeBotCost[0], clay//geodeBotCost[1]) + 1):
                        # print('buildOreBots', buildOreBots, 'buildClayBots', buildClayBots, 'buildObsidianBots', buildObsidianBots, 'buildGeodeBots', buildGeodeBots)
                        dfs(elapsedTime + 1, ore - (buildOreBots * oreBotCost[0]) - (buildClayBots * clayBotCost[0]) - (buildObsidianBots * obsidianBotCost[0]) - (buildGeodeBots * geodeBotCost[0]) + oreBots, \
                            clay - (buildObsidianBots * obsidianBotCost[1]) + clayBots, obsidian - (buildGeodeBots * geodeBotCost[1]) + obsidianBots, geodes + geodeBots, \
                            oreBots + buildOreBots, clayBots + buildClayBots, obsidianBots + buildObsidianBots, geodeBots + buildGeodeBots)
        return
    '''



    dfs(0, 0, 0, 0, 0, 1, 0, 0, 0)
    qualityLevels.append(blueprintID * maxGeodes[0])

print(sum(qualityLevels))

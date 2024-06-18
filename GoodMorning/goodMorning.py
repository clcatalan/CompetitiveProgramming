keyboard = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['x', '0', 'x'],
]

keyDict = {
    '1': [0,0],
    '2': [0,1],
    '3': [0,2],
    '4': [1,0],
    '5': [1,1],
    '6': [1,2],
    '7': [2,0],
    '8': [2,1],
    '9': [2,2],
    '0': [3,1]
}

keyValidNeighbors = {
    '1': ['1','2','3','4','5','6','7','8','9','0'],
    '2': ['2','3','5','6','8','9','0'],
    '3': ['3','6','9'],
    '4': ['4','5','6','7','8','9','0'],
    '5': ['5','6','7','8','9','0'],
    '6': ['6','9'],
    '7': ['7','8','9','0'],
    '8': ['8','9','0'],
    '9': ['9'],
    '0': ['0']
}

DIFF = 99999

def getNeighbors(vRow, vCol):
    neighbors = []

    vBelow = vRow + 1
    vRight = vCol + 1

    if vBelow <= 3:
        below = (vBelow, vCol)
        neighbors.append(below)

    if vRight <= 2:
        right = (vRow, vRight)
        neighbors.append(right)

    return neighbors    

def isValidNeighbor(prev, curr):
    prevC = keyDict[prev]
    currC = keyDict[curr]

    # if curr's row is below prev's, then valid
    if currC[0] >= prevC[0] and currC[1] ==  prevC[1]:
        return True
    # if curr's row is right of prev's, then valid
    if currC[1] >= prevC[1] and currC[0] == prevC[0]:
        return True
    # if curr's row and col is below and right of prev's, then valid
    if currC[1] >= prevC[1] and currC[0] >= prevC[0]:
        return True
    
    return False

def search(target, targetTokens):
    global DIFF
    res = []
    temp = []
    for i in range(len(targetTokens)):
        t = targetTokens[i]
        if i > 0:
            if isValidNeighbor(res[i-1], t):
                #print('append')
                res.append(t)
                temp.append(t)
            else:
                #print('search for others')
                neighbors = keyValidNeighbors[res[i-1]]
                temp.append(neighbors[0])
                res.append(neighbors[0])
                for n in neighbors:
                    temp[i] = n
                    tempInt = int("".join(temp))
                    if abs(target-tempInt) < DIFF:
                        DIFF = abs(target-tempInt)
                        res[i] = n

        else:
            #print('append first')
            res.append(t)
            temp.append(t)

    return int("".join(res))

def main():
    global DIFF
    t = int(input())
    visited = [False]*10
    for i in range(t):
        DIFF = 99999
        target = int(input())
        targetStr = str(target)
        targetTokens = [c for c in targetStr]
        # print(k)
        res = search(int(target), targetTokens)
        print(res)



    

main()
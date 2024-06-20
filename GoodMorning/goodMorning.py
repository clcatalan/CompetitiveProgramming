keyValidNeighbors = {
    '1': ['1','2','3','4','5','6','7','8','9','0'],
    '2': ['2','3','5','6','8','9','0'],
    '3': ['3','6','9'],
    '4': ['4','5','6','7','8','9','0'],
    '5': ['5','6','8','9','0'],
    '6': ['6','9'],
    '7': ['7','8','9','0'],
    '8': ['8','9','0'],
    '9': ['9'],
    '0': ['0']
}

def isValidCombination(target):
    targetTokens = [t for t in str(target)]
    for i in range(1, len(targetTokens)):
        curr = targetTokens[i]
        prev = targetTokens[i-1]

        if not curr in keyValidNeighbors[prev]:
            return False
    return True


def main():
    t = int(input())
    for i in range(t):
        target = int(input())
        
        j = 0
        while not isValidCombination(target+j) and not isValidCombination(target-j):
            j += 1
        
        if isValidCombination(target+j):
            print(target+j)
        else:
            print(target-j)
        






    

main()
import math

def buildAdjList(N, L):
    adjList = {}

    for i in range(N):
        adjList[i] = []

    for i in range(L):
        pair = [int(e) for e in input().split()]
        a, b = pair

        if not a in adjList:
            adjList[a] = []

        adjList[a].append(b)    
        
        if not b in adjList:
            adjList[b] = []

        adjList[b].append(a)

    return adjList




def main():
    # global maxIndex
    inputs = input().split()
    N = int(inputs[0])
    H = int(inputs[1])
    L = int(inputs[2])
    
    horrorIds = [int(x) for x in input().split()]
    
    #create dictionary for Horror Indices of Movies
    HI = {}
    for e in horrorIds:
        HI[e] = 0

    #buildAdjList
    adjList = buildAdjList(N, L)
    

    # print('adjacency list')
    # for vertex, neighbors in adjList.items():
    #     print(f"{vertex} -> {' '.join(map(str, neighbors))}")


    #bfs
    queue = horrorIds
    while(queue):
        i = queue.pop(0)
        if i in adjList:
            for j in adjList[i]:
                if not j in HI:
                    HI[j] = HI[i] + 1
                    queue.append(j)

    # print('Horror Indices')
    # for vertex, val in HI.items():
    #     print(f"{vertex} -> {val}")


    maxValue = 0
    maxIndex = 0

    for i in range(N):
        if not i in HI and float('inf') > maxValue:
            maxValue = float('inf')
            maxIndex = i
        elif i in HI and HI[i] > maxValue:
            maxValue = HI[i]
            maxIndex = i
        # print(i, maxValue, maxIndex)

    print(maxIndex)



    

    


    

    
main()
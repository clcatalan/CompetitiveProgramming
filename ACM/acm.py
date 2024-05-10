#https://open.kattis.com/problems/acm
from sys import stdin

pDict = {}
wDict = {}
line = ''
def main():
    line = ''
    score = 0
    right = 0
    
    while line!='-1':
        line = input()
        if line != '-1':
            m, p, c = line.split()
            pDict[p] = int(m)
            if(c == 'right'):
                score += pDict[p]
                right += 1
                if(p in wDict):
                    score += (20*wDict[p])
            elif(c == 'wrong'):
                if(p in wDict):
                    wDict[p] += 1
                else:
                    wDict[p] = 1

   

    # print(pDict)
    # print(wDict)
    print(right, score)
main()
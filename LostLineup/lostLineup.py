#https://open.kattis.com/problems/lostlineup
def main():
    n = int(input())
    people = input().split()
    #print(people)
    res = [0] * n
    res[0] = 1
    for i, p in enumerate(people):
        #print(i, p)
        res[int(p)+1] = i+2

    for r in res:
        print(r, end=" ")    
        
main()
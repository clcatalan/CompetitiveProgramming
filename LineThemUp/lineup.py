#https://open.kattis.com/problems/lineup
def main():
    n = int(input())
    res = 'NEITHER'
    names = []
    for i in range(n):
        line = input()
        names.append(line)
    
    if(all(names[i] <= names[i+1] for i in range(n-1))):
        res = 'INCREASING'
    elif(all(names[i] > names[i+1] for i in range(n-1))):
        res = 'DECREASING'

    print(res) 
main()
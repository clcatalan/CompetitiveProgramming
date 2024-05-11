def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    
    d = min(a[1] - a[0], a[2] - a[1])
    res = a[0] + (3*d)
    if(a[1]-a[0] != d):
        res = a[0]+d
    if(a[2]-a[1] != d):
        res = a[1]+d

    print(res)    
        
    
main()
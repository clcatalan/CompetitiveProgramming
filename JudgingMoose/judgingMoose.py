def main():
    l, r = map(int, input().split())
    #res = 'Even ' + str(l+r) if l == r else 'Odd ' + str(2*max(l,r))
    
    if l == 0 and r == 0:
        print('Not a moose')
        return
    
    if l == r:
        print('Even ' + str(l+r))
    else:
        print('Odd ' + str(2*max(l,r)))
    
main()
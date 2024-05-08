def main():
    n,m = map(int, input().split())
    pcs = ' pieces ' if abs(n-m) > 1 else ' piece '
    if n <= m:
        print('Dr. Chaz will have ' + str(abs(n-m)) + pcs + 'of chicken left over!')
    else:
        print('Dr. Chaz needs ' + str(abs(n-m)) + ' more' + pcs + 'of chicken!')
    
main()
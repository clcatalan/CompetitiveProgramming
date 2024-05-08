def main():
    m, d = input().split()
    res = 'yup' if ((m == 'OCT' and d == '31') or (m == 'DEC' and d == '25')) else 'nope'
    print(res)

main()
# Solution:
# 1. Generate all permutations of num
# 2. compare each permutation with each other, to see which is the smallest value bigger than num


#moved these three lines here from main, but still getting UnboundLocalError
global MIN_NUM
MIN_NUM = 9999

def permutation(num, i = 0):
    if i == len(num):
        res = int("".join(num))
        if res < MIN_NUM:
            MIN_NUM = res
        return
    else:
        for j in range(i, len(num)):
            num[i], num[j] = num[j], num[i]
            permutation(num, i + 1)
            num[j], num[i] = num[i], num[j]

def main():

    x = input()
    origNum = int(x)
    num = [c for c in x]
    #generate all permutations then compare each permutation with each other to global MIN_NUM to find smallest number
    permutation(num)

    #check if the smallest permutation is still bigger than the origNum
    if(MIN_NUM > origNum):
        print(MIN_NUM)
    else:
        print(0)

main()


    
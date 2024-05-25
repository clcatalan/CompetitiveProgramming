def permutation(validPermutations, origNum, num, i = 0):
    if i == len(num):
        res = int("".join(num))
        if res > origNum:
            validPermutations.append(res)
        return
    else:
        for j in range(i, len(num)):
            num[i], num[j] = num[j], num[i]
            permutation(validPermutations, origNum, num, i + 1)
            num[j], num[i] = num[i], num[j]

def main():
    MIN_NUM = 9999
    x = input()
    origNum = int(x)
    num = [c for c in x]

    validPermutations = []
    permutation(validPermutations, origNum, num)


    if len(validPermutations) > 0:
        print(min(validPermutations))
    else:
        print(0)

main()

import math
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        r = int((math.sqrt(1+(8*n))-1)/2)
        print(r)
main()
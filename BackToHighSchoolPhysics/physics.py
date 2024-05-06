from sys import stdin

def main():
    for line in stdin:
        v,t = map(int, line.split())
        print(v*(2*t))
main()
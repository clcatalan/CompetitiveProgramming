#https://open.kattis.com/problems/fizzbuzz
def main():
    x,y,n = map(int, input().split())
    
    for i in range(1,n+1):
        if(i%x == 0 and i%y != 0):
            print('Fizz')
        elif(i%y == 0 and i%x != 0):
            print('Buzz')
        elif(i%x == 0 and i%y == 0):
            print('FizzBuzz')
        else:
            print(i)
        
main()
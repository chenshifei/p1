from math import sqrt

def find_root(n):
    guess = 1
    for i in range(10):
        guess = (n / guess + guess) / 2.0
        print('After iteration', (i + 1) , 'my guess is', guess)

def main():
    num = input('Please input an integer and I will try to guess its root. ')
    find_root(int(num))
    print('And the acutal square root of that number is', sqrt(int(num)))

main()

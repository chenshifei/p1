def greet(name):
    print('Hello', name, '!')
    if len(name) > 7:
        print('You have a really long name!')

def f(n, m):
    if n == m:
        print('The numbers are the same.')
    if n % 2 != 0:
        print('The first number is odd.')
    if n > 99 and m > 99:
        print('Both numbers are big.')

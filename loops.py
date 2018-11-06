sum = 0

for n in range(10):
    sum += n

print('The sum of the numbers is ' + str(sum))

for n in range(5, 12):
    for _ in range(n):
        print('X', end='')
    print()

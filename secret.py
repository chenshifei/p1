from random import randint

def comment(n):
    if n < 1:
        return 'You are a genius! Or can you read people\'s mind?'
    elif n < 3:
        return 'That\'s great! Less than I thought.'
    elif n < 6:
        return 'Than\'s good!'
    else:
        return 'Hmmm, bad luck. Maybe it\'s gonna be better next time.'

def game():
    answer = randint(0, 100)
    print('Let\'s try to guess a number between 0 and 100')
    count = 0
    guess = -1
    while not guess == answer:
        guess = int(input('What is your guess? '))
        if guess < answer:
            print('That is too low.')
        elif guess > answer:
            print('That is too high.')
        count += 1
    else:
        print('Congrates! You have found the right number in', count, 'steps!')
        print(comment(count))

game()

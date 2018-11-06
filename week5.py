def mymin(numbers):
    result = numbers[0]
    for i in numbers:
        if i < result:
            result = i
    return result

def long(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

def histogram(numbers, char):
     for i in numbers:
         print(i * char)

def odd_even(numbers):
    odds = []
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return odds + evens

def allit(words):
    c = words[0][0].lower()
    for word in words:
        if word[0].lower != c:
            return False
    return True

def anti_allit(words):
    initials = []
    for word in words:
        if word[0].lower() in initials:
            return False
        else:
            initials.append(word[0].lower())
    return True

def endings(word):
    result = []
    for i in range(len(word)):
        result.append(word[i:])
    return result

def vhistogram(numbers, char):
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    for line in range(max_number):
        for n in numbers:
            if n + line >= max_number:
                print(char, end='')
            else:
                print(' ', end='')
        print()

def longestword(text):
    words = text.split()
    result = words[0]
    for word in words:
        if len(word) > len(result):
            result = word
    return result

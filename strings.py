def indef(text):
    article = 'a'
    if (text[0].lower() in 'aeiou'):
        article = 'an'
    return article + ' ' + text

def parens(s):
    result = ''
    for c in s:
        result += '(' + c + ')'
    return result

def wordtriangle(word):
    for i in range(len(word)):
        print(word[:i + 1])

def cutstring(s, i):
    return s[i:] + s[:i]

def upper_after_space(s):
    result = ''
    seen_space = False
    for i in range(len(s)):
        if seen_space:
            result = result + s[i].upper()
            seen_space = False
        else:
            result = result + s[i]
        if s[i] == ' ':
            seen_space = True
    return result

def upper_after_space_improved(s):
    result = ''
    for i in range(0, len(s)):
        if s[i - 1] == ' ' and i != 0:
            result += s[i].upper()
        else:
            result += s[i]
    return result

def is_palindrome(s):
    l = len(s)
    for i in range(int(l/2)):
        if s[i].lower() != s[l - i - 1].lower():
            return False
    return True

def is_palindrome_improved(s):
    return s.lower() == s[::-1].lower()

def countmatch(s1, s2):
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return i
    return min_len

def grid(s):
    for i in range(len(s)):
        print(s[i:] + s[:i])

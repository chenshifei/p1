from nltk.corpus import gutenberg

alice = gutenberg.sents('carroll-alice.txt')

def count_word():
    result = {}
    for sentence in alice:
        for word in sentence:
            normalized_word = word.lower()
            if normalized_word.isalpha():
                result[normalized_word] = result.setdefault(normalized_word, 0) + 1
    return result

def count_first_word():
    result = {}
    for sentence in alice:
        first_word = sentence[0]
        first_word = first_word.lower()
        if first_word.isalpha():
            result[first_word] = result.setdefault(first_word, 0) + 1
    return result

def count():
    wordf = count_word()
    firstf = count_first_word()

    words = sorted(wordf.keys())
    for word in words:
        count = wordf[word]
        if count >= 100:
            count_first = firstf.get(word, 0)
            percentage = count_first / count * 100
            print('{:10} {:3} {:4} {:4.0f}%'.format(word, count_first, count, percentage))

count()

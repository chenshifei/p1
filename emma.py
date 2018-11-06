from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')

for sentence in emma:
    if len(sentence) < 3:
        continue
    if sentence[0].casefold() == sentence[2].casefold():
        print(' '.join(sentence))

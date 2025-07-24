# create a list of words lengths
phrase = "the quick brown fox jumps over the lazy dog"

# regular way
wordList = phrase.split()
wordLengths = []
for word in wordList:
    if word != "the":
        wordLengths.append(len(word))

# comprehension notation (linq style)
words = phrase.split()
lengths = [len(word) for word in words if word != "the"]
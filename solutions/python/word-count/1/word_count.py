import re

def count_words(sentence):
    words = re.split(r"[^a-zA-Z0-9']+", sentence.lower())
    counts = {}

    for word in words:
        word = word.strip("'")
        if word:
            counts[word] = counts.get(word, 0) + 1

    return counts

import string
from collections import Counter

def is_pangram(sentence):
    letters = Counter([item for item in string.ascii_lowercase])

    char_register = Counter([char for char in sentence.lower()])

    for key in letters.keys():
        if key not in char_register.keys():
            return False

    return True

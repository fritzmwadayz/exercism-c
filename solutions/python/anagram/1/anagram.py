from collections import Counter as c

def find_anagrams(word, candidates):
    result = []
    word_counter = c(word.lower())
    
    for candidate in candidates:
        if candidate.lower() != word.lower() and c(candidate.lower()) == word_counter:
            result.append(candidate)

    return result

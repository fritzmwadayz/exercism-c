def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ')
    tokens = words.split()

    result = [token[0].upper() for token in tokens]

    return ''.join(result)

from itertools import zip_longest

def transpose(text):
    rows = text.splitlines()
    
    max_len = max((len(row) for row in rows), default=0)
    valid_lengths = [0] * max_len

    for index, row in enumerate(rows):
        for i in range(len(row)):
            valid_lengths[i] = index + 1
            
    return '\n'.join(
        ''.join(column)[:valid_lengths[i]]
        for i, column in enumerate(zip_longest(*rows, fillvalue=' '))
    )

    
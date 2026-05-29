def score(word):
    ones = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    twos = ['D', 'G']
    threes = ['B', 'C', 'M', 'P']
    fours = ['F', 'H', 'V', 'W', 'Y']
    fives = ['K']
    eights = ['J', 'X']
    tens = ['Q', 'Z']

    count = 0
    for char in word:
        if char.upper() in ones:
            count += 1
        elif char.upper() in twos:
            count += 2
        elif char.upper() in threes:
            count += 3
        elif char.upper() in fours:
            count += 4
        elif char.upper() in fives:
            count += 5
        elif char.upper() in eights:
            count += 8
        elif char.upper() in tens:
            count += 10

    return count

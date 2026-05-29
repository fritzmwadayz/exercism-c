def score(word):
    groups = [
        (1, ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']),
        (2, ['D', 'G']),
        (3, ['B', 'C', 'M', 'P']),
        (4, ['F', 'H', 'V', 'W', 'Y']),
        (5, ['K']),
        (8, ['J', 'X']),
        (10, ['Q', 'Z']),
    ]
    score_map = {}
    for points, letters in groups:
        for letter in letters:
            score_map[letter] = points
    
    return sum(score_map.get(char.upper(), 0) for char in word)

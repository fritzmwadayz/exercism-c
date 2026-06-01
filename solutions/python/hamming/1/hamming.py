def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0

    char_a, char_b = 0, 0

    while char_a < len(strand_a):
        if strand_a[char_a] != strand_b[char_b]:
            count += 1
        char_a += 1
        char_b += 1

    return count

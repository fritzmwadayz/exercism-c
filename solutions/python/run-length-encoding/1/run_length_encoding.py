def decode(string):
    posn = 0
    factor = []
    result = []

    while posn < len(string):
        if string[posn].isdigit():
            factor.append(string[posn])
        else:
            if len(factor) != 0:
                multiplier = int(''.join(factor))
                result.append(string[posn]*multiplier)
                factor = []
            else:
                result.append(string[posn])
        posn += 1

    return ''.join(result)


def encode(string):
    if len(string) == 0:
        return string
        
    result = []
    current = string[0]
    count = 1

    for char in string[1:]:
        if char == current:
            count += 1
        else:
            if count > 1:
                result.append(f'{count}{current}')
            else:
                result.append(current)
            current = char
            count = 1
    if count > 1:
        result.append(f'{count}{current}')
    else:
        result.append(current)

    return ''.join(result)
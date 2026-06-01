def value(colors):
    colors = colors[:2]

    value_map = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange': '3',
        'yellow': '4',
        'green': '5',
        'blue': '6',
        'violet': '7',
        'grey': '8',
        'white': '9',
    }

    mapping = []

    if colors[0] == 'black':
        return int(value_map[colors[1]])

    for color in colors:
        mapping.append(value_map[color])

    return int(''.join(char for char in mapping))

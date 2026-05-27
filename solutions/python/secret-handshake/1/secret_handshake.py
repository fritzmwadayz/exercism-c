def commands(binary_str):
    actions = [
            'wink',
            'double blink',
            'close your eyes',
            'jump'
        ]

    action = 0
    i = len(binary_str) - 1

    result = []

    while i > 0:
        if binary_str[i] == '1':
            result.append(actions[action])

        i -= 1
        action += 1

    if binary_str[0] ==  '1':
        result.reverse()

    return result
        

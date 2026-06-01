def is_paired(input_string):
    stack = []

    pairs = {
        '}':'{',
        ']':'[',
        ')':'('
    }

    for char in input_string:
        if char in '({[':
            stack.append(char)
        elif char in ']})':
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

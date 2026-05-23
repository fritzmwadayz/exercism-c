def is_isogram(string):
    result = ''.join(char for char in string.lower() if char.isalpha())
    unique = set()

    for char in result:
        if char in unique:
            return False
        unique.add(char)

    return True

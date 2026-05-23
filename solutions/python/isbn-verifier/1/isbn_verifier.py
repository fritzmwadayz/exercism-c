import string

def is_valid(isbn):
    cleaned = isbn.replace("-", "")

    if len(cleaned) != 10:
        return False

    total = 0
    multiplier = 10

    for char in cleaned:
        if char.isdigit():
            total += int(char) * multiplier
        elif char == 'X' and multiplier == 1:
            total += 10 * multiplier
        else:
            return False
            
        multiplier -= 1

    return total % 11 == 0

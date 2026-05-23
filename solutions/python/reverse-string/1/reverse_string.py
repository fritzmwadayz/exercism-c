def reverse(text):
    chars = [s for s in text]
    first, last = 0, len(chars)-1

    while first < last:
        chars[first], chars[last] = chars[last], chars[first]
        first += 1
        last -= 1
        
    return ''.join(char for char in chars)

import string

def rotate(text, key):
    alphabet = string.ascii_lowercase
        
    rotated = alphabet[key:]+alphabet[:key]
    result = []

    map = {}
    
    for i, char in enumerate(alphabet):
        map[char] = rotated[i]

    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(map[char.lower()].upper())
            else:
                result.append(map[char.lower()])
        else:
            result.append(char)
            
    return ''.join(char for char in result)

import string

def rotate(text, key):
    alphabet = string.ascii_lowercase
        
    rotated = alphabet[key:]+alphabet[:key]
    result = []

    cipher = {}
    
    for i, char in enumerate(alphabet):
        cipher[char] = rotated[i]

    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(cipher[char.lower()].upper())
            else:
                result.append(cipher[char.lower()])
        else:
            result.append(char)
            
    return ''.join(char for char in result)

import string
ALPHABET = [char for char in string.ascii_lowercase]
REVERSED = list(string.ascii_lowercase)[::-1]
CIPHER = dict(zip(ALPHABET, REVERSED))
    
def encode(plain_text):
    transformed = []
    for ch in plain_text:
        if ch.isalpha():
            transformed.append(CIPHER[ch.lower()])
        elif ch.isdigit():
            transformed.append(ch)

    result = []
    for i, ch in enumerate(transformed):
        if i > 0 and i % 5 == 0:
            result.append(' ')
        result.append(ch)
    return ''.join(result)


def decode(ciphered_text):
    result = []
    for ch in ciphered_text:
        if ch.isalpha():
            result.append(CIPHER[ch.lower()])
        elif ch.isdigit():
            result.append(ch)
    return ''.join(result)

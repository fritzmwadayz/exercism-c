import string
import random
letters = string.ascii_lowercase

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(letters) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        if not self.key:
            return text

        shifts = [letters.find(ch) for ch in self.key.lower() if ch in letters]
        if not shifts:
            return text

        encoded_chars = []
        key_index = 0
        for ch in text:
            if ch.lower() in letters:
                shift = shifts[key_index % len(shifts)]
                base = ord('a') if ch.islower() else ord('A')
                original_pos = ord(ch) - base
                new_pos = (original_pos + shift) % 26
                encoded_chars.append(chr(base + new_pos))
                key_index += 1
            else:
                encoded_chars.append(ch)
        return ''.join(encoded_chars)

    def decode(self, text):
        if not self.key:
            return text

        shifts = [letters.find(ch) for ch in self.key.lower() if ch in letters]
        if not shifts:
            return text

        decoded_chars = []
        key_index = 0
        for ch in text:
            if ch.lower() in letters:
                shift = shifts[key_index % len(shifts)]
                base = ord('a') if ch.islower() else ord('A')
                original_pos = ord(ch) - base
                new_pos = (original_pos - shift) % 26
                decoded_chars.append(chr(base + new_pos))
                key_index += 1
            else:
                decoded_chars.append(ch)
        return ''.join(decoded_chars)


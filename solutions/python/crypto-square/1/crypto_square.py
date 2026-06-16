import math
import re
from itertools import zip_longest

def cipher_text(plain_text):
    normalized = re.sub(r'[^a-z0-9]', '', plain_text.lower())
    if not normalized:
        return ""
        
    c = math.ceil(math.sqrt(len(normalized)))
    r = math.ceil(len(normalized) / c)

    rows = [normalized[i:i+c] for i in range(0, len(normalized), c)]
    columns = [''.join(col) for col in zip_longest(*rows, fillvalue=' ')]

    return ' '.join(columns)
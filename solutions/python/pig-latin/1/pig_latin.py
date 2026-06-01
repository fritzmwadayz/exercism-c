def translate(text):
    vowels = set('aeiou')
    words = text.split()
    pig_words = []
    for word in words:
        pig_words.append(translate_word(word))
    return ' '.join(pig_words)

def translate_word(word):
    vowels = set('aeiou')
    
    if word[0] in vowels or word.startswith(('xr', 'yt')):
        return word + 'ay'

    qu_pos = word.find('qu')
    if qu_pos != -1:
        before_qu = word[:qu_pos]
        if all(c not in vowels for c in before_qu):
            prefix = word[:qu_pos+2]
            rest = word[qu_pos+2:]
            return rest + prefix + 'ay'
    
    for i, ch in enumerate(word):
        if ch == 'y' and i > 0:
            has_vowel = any(c in vowels for c in word[:i])
            if not has_vowel:
                prefix = word[:i]
                rest = word[i:]
                return rest + prefix + 'ay'
    
    for i, ch in enumerate(word):
        if ch in vowels:
            prefix = word[:i]
            rest = word[i:]
            return rest + prefix + 'ay'
    
    return word + 'ay'

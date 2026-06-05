def recite(start, take=1):
    NUMBERS = [
        'no', 'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine', 'ten'
    ]
    
    def bottle_word(n):
        return "bottle" if n == 1 else "bottles"
    
    def line(n):
        word = NUMBERS[n].title() if n > 0 else NUMBERS[n]
        return f"{word} green {bottle_word(n)} hanging on the wall,"
    
    verses = []
    for i in range(take):
        current = start - i
        if current < 1:
            break
            
        next_num = current - 1
        
        if i > 0:
            verses.append("")
            
        first = line(current)
        last = f"There'll be {NUMBERS[next_num]} green {bottle_word(next_num)} hanging on the wall."
        
        verses.extend([first, first, "And if one green bottle should accidentally fall,", last])
    
    return verses

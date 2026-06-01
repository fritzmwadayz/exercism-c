def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"

    ones = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen'
    }
    
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    def say_chunk(n):
        parts = []
        
        if n >= 100:
            parts.append(ones[n // 100])
            parts.append("hundred")
            n %= 100
        
        if n >= 20:
            word = tens[n // 10]
            if n % 10 != 0:
                word += "-" + ones[n % 10]
            parts.append(word)
        elif n > 0:
            parts.append(ones[n])
        
        return " ".join(parts)

    scales = ["", "thousand", "million", "billion"]
    chunks = []
    scale_index = 0
    
    while number > 0:
        chunk = number % 1000
        if chunk != 0:
            text = say_chunk(chunk)
            if scales[scale_index]:
                text += " " + scales[scale_index]
            chunks.append(text)
        number //= 1000
        scale_index += 1
    
    chunks.reverse()
    return " ".join(chunks)
    

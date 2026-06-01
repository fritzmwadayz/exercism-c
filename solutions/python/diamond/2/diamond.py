def rows(letter):
    n = ord(letter) - ord('A')
    
    upper_rows = []
    
    for i in range(n + 1):
        current_char = chr(ord('A') + i)
        outer_spaces = ' ' * (n - i)
        
        if i == 0:
            middle = current_char
        else:
            inner_spaces = ' ' * (2 * i - 1)
            middle = current_char + inner_spaces + current_char
            
        row = outer_spaces + middle + outer_spaces
        upper_rows.append(row)
        
    bottom_rows = upper_rows[-2::-1]
    
    return upper_rows + bottom_rows
    

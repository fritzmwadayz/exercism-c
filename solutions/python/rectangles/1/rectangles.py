
def valid_edge(chars, allowed):
    return all(c in allowed for c in chars)
    
def rectangles(strings):
    count = 0
    for row_index, row in enumerate(strings):
        for c1 in range(len(row)):
            for c2 in range(c1 + 1, len(row)):
                if row[c1] == '+' and row[c2] == '+':
                    for r2 in range(row_index+1, len(strings)):
                        top = row[c1:c2+1]
                        bottom = strings[r2][c1:c2+1]
                        
                        left = [strings[r][c1] for r in range(row_index, r2+1)]
                        right = [strings[r][c2] for r in range(row_index, r2+1)]
                        
                        if (valid_edge(top, '-+') and 
                            valid_edge(bottom, '-+') and 
                            valid_edge(left, '|+') and 
                            valid_edge(right, '|+')):
                            count += 1
    
    return count
        
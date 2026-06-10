def saddle_points(matrix):
    if not matrix:
        return []
    first_row_length = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != first_row_length:
            raise ValueError("irregular matrix")
            
    columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]    
    result = []
    
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if value == max(row) and value == min(columns[c]):
                result.append({"row": r + 1, "column": c + 1})
    return result
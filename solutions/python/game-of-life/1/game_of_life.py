def tick(matrix):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    columns = len(matrix[0])

    result = [[0]*columns for _ in range(rows)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for row in range(rows):
        for column in range(columns):
            live_neighbors = 0
            for dr, dc in directions:
                new_row = row + dr
                new_column =  column + dc
                if 0 <= new_row < rows and 0 <= new_column < columns:
                    live_neighbors += matrix[new_row][new_column]
            current = matrix[row][column]
            if current == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    result[row][column] = 1
                else:
                    result[row][column] = 0
            else:
                if live_neighbors == 3:
                    result[row][column] = 1
                else:
                    result[row][column] = 0
    return result

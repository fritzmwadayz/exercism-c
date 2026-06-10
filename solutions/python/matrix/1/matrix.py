class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = [entry for entry in self.matrix_string.split("\n")]
        row_string = rows[index-1]
        return [int(x) for x in row_string.split()]

    def column(self, index):
        result = []
        rows = [entry for entry in self.matrix_string.split("\n")]
        for row in rows:
            entries = row.split()
            result.append(int(entries[index-1]))
        return result

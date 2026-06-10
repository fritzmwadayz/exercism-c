class Queen:
    def __init__(self, row, column):
        self.row = self._validate(row, "row")
        self.column = self._validate(column, "column")
    def _validate(self, value, name):
        if value < 0:
            raise ValueError(f"{name} not positive")
        if value > 7:
            raise ValueError(f"{name} not on board")
        return value

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row-another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False

from collections import deque

class ConnectGame:
    def __init__(self, board):
        rows = board.splitlines()
        self.grid = [row.strip().replace(' ', '') for row in rows]
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0]) if self.grid else 0

    def get_winner(self):
        # O plays top to bottom: start from row 0, goal is last row
        o_starts = [(0, c) for c in range(self.n_cols)]
        if has_path(self.grid, 'O', o_starts, self.n_rows, self.n_cols, goal_row=self.n_rows - 1):
            return "O"

        # X plays left to right: start from column 0, goal is last column
        x_starts = [(r, 0) for r in range(self.n_rows)]
        if has_path(self.grid, 'X', x_starts, self.n_rows, self.n_cols, goal_col=self.n_cols - 1):
            return "X"

        return ""


def neighbors(r, c, n_rows, n_cols):
    offsets = [(0, -1), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 0)]
    result = []
    for dr, dc in offsets:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n_rows and 0 <= nc < n_cols:
            result.append((nr, nc))
    return result
    
def has_path(grid, player, starts, n_rows, n_cols, goal_row=None, goal_col=None):
    visited = set()
    queue = deque()
        
    for r, c in starts:
        if grid[r][c] == player:
            queue.append((r, c))
            visited.add((r, c))
        
    while queue:
        r, c = queue.popleft()
        if goal_row is not None and r == goal_row:
            return True
        if goal_col is not None and c == goal_col:
            return True
        for nr, nc in neighbors(r, c, n_rows, n_cols):
            if (nr, nc) not in visited and grid[nr][nc] == player:
                visited.add((nr, nc))
                queue.append((nr, nc))
       
    return False
        
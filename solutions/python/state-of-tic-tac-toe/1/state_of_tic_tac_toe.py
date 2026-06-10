def gamestate(board):
    n = len(board)
    rows = board
    columns = [''.join(row[i] for row in board) for i in range(n)]
    main_diagonal = ''.join(board[i][i] for i in range(n))
    anti_diagonal = ''.join(board[i][n-1-i] for i in range(n))
    lines = rows + columns + [main_diagonal, anti_diagonal]

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    x_won = _has_won('X', lines)
    o_won = _has_won('O', lines)

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_count-o_count > 1:
        raise ValueError("Wrong turn order: X went twice")
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_won or o_won:
        return "win"
    for row in board:
        if ' ' in row:
            return "ongoing"
    return "draw"

def _has_won(player, lines):
    for entry in lines:
        if set(entry) == {player}:
            return True
    return False
    
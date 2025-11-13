def print_board(board):
    line = "---+---+---"
    def cell(i): return f" {board[i]} "
    print(cell(0) + "|" + cell(1) + "|" + cell(2))
    print(line)
    print(cell(3) + "|" + cell(4) + "|" + cell(5))
    print(line)
    print(cell(6) + "|" + cell(7) + "|" + cell(8))

board = [
    'X', ' ', 'O',
    ' ', 'X', 'O',
    ' ', ' ', 'O'
]

print("Current Tic-Tac-Toe Board:")
print_board(board)
moves = [
    ('X', 1),
    ('O', 3),
    ('X', 5),
    ('O', 6),
    ('O', 9)
]
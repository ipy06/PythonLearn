EMPTY = "-"
ROOK = "R"
PAWN = "P"
KNIGHT = "L"
BISHOP = "B"
BQUEEN = "BQ"
BKING = "BK"
WQUEEN = "WQ"
WKING = "WK"


board = [[EMPTY for i in range(8)]for j in range(8)]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

for i in range(8):board[1][i]=PAWN
for i in range(8):board[6][i]=PAWN

board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT


board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP

board[0][3] = BQUEEN
board[0][4] = BKING

board[7][3] = WQUEEN
board[7][4] = WKING


print(board)

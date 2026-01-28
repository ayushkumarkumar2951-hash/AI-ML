N = 8;
def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    
    return True

def solve_queens(board, col):
    if col == N:
        print(board)
        return True
    
    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            if solve_queens(board, col + 1):
                return True
            board[col] = -1
            
    return False

board = [-1] * N
solve_queens(board, 0)
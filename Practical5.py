N = 8

def check(board, r, c):
    for i in  range(c):
        if board[r][i] == 1:
            return False

    i = r-1
    j = c-1

    while i>=0 and j>=0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = r+1
    j = c-1

    while i<N and j>=0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_N_queen(board, count):
    if count == N:
        for row in board:
            print(row)
        print("_" * 20)
        return

    for i in range(N):
        if check(board,i,count):
            board[i][count] = 1
            solve_N_queen(board, count + 1)
            board[i][count] = 0

    return

board = [[0]*N for _ in range(N)]
solve_N_queen(board,0)

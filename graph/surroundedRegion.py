def solve(board):
        MAX_ROWS = len(board)
        MAX_COLS = len(board[0])

        def dfs(row, col):
            if (row < 0 or col < 0 or row == MAX_ROWS or col == MAX_COLS  or board[row][col] != "O"):
                return
            board[row][col] = "T"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        print(board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (board[row][col] == "O" and ((row == 0 or row == MAX_ROWS - 1) 
                or (col == 0 or col == MAX_COLS - 1))):
                    dfs(row, col)
        print(board)

        for row in range(MAX_ROWS):
            for col in range(MAX_COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
        print(board)

        for row in range(MAX_ROWS):
            for col in range(MAX_COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
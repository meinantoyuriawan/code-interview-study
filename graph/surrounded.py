
# reverse thinking
def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    rows, cols = len(board), len(board[0])
    visited = set()

    def traverse(i,j):

        if (
            (i,j) in visited or
            i<0 or j<0 or
            i== rows or j== cols or
            board[i][j] != "O"
        ):
            return
        board[i][j] = "T"
        visited.add((i,j))
        traverse(i+1,j)
        traverse(i,j+1)
        traverse(i-1,j)
        traverse(i,j-1)

    for i in range(rows):
        traverse(i, 0)
        traverse(i,cols-1)

    for j in range(cols):
        traverse(0, j)
        traverse(rows-1, j)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "T":
                board[r][c] = "O"

    print(board)



# board = [
#     ["X","O","X","O","X","O"],
#     ["O","X","O","X","O","X"],
#     ["X","O","X","O","X","O"],
#     ["O","X","O","X","O","X"]]

# board = [
#     ["X","O","X","O","X","O","O","O","X","O"],
#     ["X","O","O","X","X","X","O","O","O","X"],
#     ["O","O","O","O","O","O","O","O","X","X"],
#     ["O","O","O","O","O","O","X","O","O","X"],
#     ["O","O","X","X","O","X","X","O","O","O"],
#     ["X","O","O","X","X","X","X","X","X","O"],
#     ["X","O","X","X","X","X","X","O","X","O"],
#     ["X","X","O","X","X","X","X","O","X","X"],
#     ["O","O","O","O","X","X","X","O","X","O"],
#     ["X","X","O","X","X","X","X","O","O","O"]
#     ]

board = [
    ["X","O","X","O","X","O","O","O","X","O"],
    ["X","O","O","X","X","X","O","O","O","X"],
    ["O","O","O","O","O","O","O","O","X","X"],
    ["O","O","O","O","O","O","X","O","O","X"],
    ["O","O","X","X","O","X","X","O","O","O"],
    ["X","O","O","X","X","X","O","X","X","O"],
    ["X","O","X","O","O","X","X","O","X","O"],
    ["X","X","O","X","X","O","X","O","O","X"],
    ["O","O","O","O","X","O","X","O","X","O"],
    ["X","X","O","X","X","X","X","O","O","O"]]

[
    ['X', 'T', 'X', 'T', 'X', 'T', 'T', 'T', 'X', 'T'], 
    ['X', 'T', 'T', 'X', 'X', 'X', 'T', 'T', 'T', 'X'], 
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'X', 'X'], 
    ['T', 'T', 'T', 'T', 'T', 'T', 'X', 'T', 'T', 'X'], 
    ['T', 'T', 'X', 'X', 'T', 'X', 'X', 'T', 'T', 'T'], 
    ['X', 'T', 'T', 'X', 'X', 'X', 'O', 'X', 'X', 'T'], 
    ['X', 'T', 'X', 'O', 'O', 'X', 'X', 'T', 'X', 'T'], 
    ['X', 'X', 'T', 'X', 'X', 'O', 'X', 'T', 'T', 'X'], 
    ['T', 'T', 'T', 'T', 'X', 'O', 'X', 'T', 'X', 'T'], 
    ['X', 'X', 'T', 'X', 'X', 'X', 'X', 'T', 'T', 'T']]

solve(board)
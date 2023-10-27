def validSudoku(board):
    # store the horizontal element and its index in 1 array
    # store the vertical element and its index in 1 array
    # store the horizontal index //3 and vertical index //3 to get the sub box index as it is reps, store the element and index in 1 array

    boxX = []
    boxY = []
    subBox = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                boxX.append((i, board[i][j]))
                boxY.append((j, board[i][j]))
                subBox.append((i//3, j//3, board[i][j]))

    def isDuplicate(arr):
        # initiate isDuplicate, if it contains duplicated element, then return false
        # so for example the boxX element is [[0,2], [1,3], [1,3]] -> there are duplicate 3 in hIndex = 1
        # length boxX = 3, length set(boxX) = 2
        setArr = set(arr)
        if len(setArr) != len(arr):
            return False
        else:
            return True
    
    return(isDuplicate(boxX) and isDuplicate(boxY) and isDuplicate(subBox))

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false

board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

print(validSudoku(board))

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]



def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    zero_row = [False] * m
    zero_col = [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_row[i] = True
                zero_col[j] = True
                
    for i in range(m):
        for j in range(n):
            if zero_row[i] or zero_col[j]:
                matrix[i][j] = 0

    return matrix

    


print(setZeroes(matrix))
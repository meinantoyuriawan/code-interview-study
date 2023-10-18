matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotateMatrix(matrix):
    # flip flip method
    # flip up to down, swap symmetry(transpose)
    m = len(matrix)
    n = len(matrix[0])

    # up to down
    # for i in range(m-1, -1, -1):
    #     print(matrix[i])

    for i in range(m//2):
        # swap matrix[i] and matrix[m-i-1]
        temp = matrix[i]
        matrix[i] = matrix[m-i-1]
        matrix[m-i-1] = temp

    for i in range(m):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)

rotateMatrix(matrix)
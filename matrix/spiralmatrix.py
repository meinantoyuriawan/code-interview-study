
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def spiralMatrix(matrix):
    res =[]
    l = 0
    r = len(matrix[0])
    t = 0
    b = len(matrix)

    while l<r and t<b :
        for j in range(l, r):
            res.append(matrix[t][j])
        t+=1
        for i in range(t, b):
            res.append(matrix[i][r-1])
        r-=1

        if not (l<r and t<b):
            break
        for j in range(r-1, l-1, -1):
            res.append(matrix[b-1][j])
        b-=1
        for i in range(b-1, t-1, -1):
            res.append(matrix[i][l])
        l+=1

    return(res)




print(spiralMatrix(matrix))
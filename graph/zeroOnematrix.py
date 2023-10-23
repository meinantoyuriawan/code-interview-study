from collections import deque

def zeroOne(mat):
    if not mat:
        return
    
    rows, cols = len(mat), len(mat[0])
    # visited = set()
    directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    ardist = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    q = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                ardist[r][c] = 0
                q.append((r,c))



    def traverse():
        while q:
            cur_i, cur_j = q.popleft()
            for di, dj in directions:
                i, j = cur_i + di, cur_j + dj

                if (i in range(rows) and 
                    j in range(cols) and 
                    ardist[i][j] > ardist[cur_i][cur_j]+1):
                    ardist[i][j] = ardist[cur_i][cur_j]+1
                    q.append((i, j))
    traverse()
    
    return ardist

# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
# mat = [
#     [0,1,0],
#     [0,1,0],
#     [0,1,0],
#     [0,1,0],
#     [0,1,0]
#     ]

res = zeroOne(mat)
print(res)
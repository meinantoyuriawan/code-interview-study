from collections import deque

def numIslands(grid):
    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

    def traverse(i, j):
        q = deque()
        visited.add((i, j))
        q.append((i, j))
        while q:
            cur_i, cur_j = q.popleft()
            for di, dj in directions:
                i, j = cur_i + di, cur_j + dj
                # conditions
                # 1. check neighbors
                # 2. grid element[i][j] == "1"
                # 3. i, j not in visited
                if (i in range(rows) and 
                    j in range(cols) and 
                    grid[i][j] == "1" and 
                    (i, j) not in visited):
                    q.append((i, j))
                    visited.add((i,j))
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                traverse(r,c)
                islands +=1
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

islands = numIslands(grid)

print(islands)
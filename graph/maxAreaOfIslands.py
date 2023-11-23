from collections import deque

def maxAreaOfIsland(grid):

    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    visited = set()

    areas = 0

    def traverse(i,j):
        area = 1
        q = deque()
        q.append((i,j))

        visited.add((i,j))
        while q:
            cur_i, cur_j = q.popleft()

            for di, dj in directions:
                nx_i, nx_j = cur_i + di, cur_j + dj

                if ((0<=nx_i<rows and 0<=nx_j<cols) and
                    ((nx_i, nx_j) not in visited) and
                    (grid[nx_i][nx_j] == 1)):
                    q.append((nx_i, nx_j))
                    visited.add((nx_i, nx_j))
                    area += 1

        return area
    
    for i in range(rows):
        for j in range(cols):
            if (((i,j) not in visited) and
                grid[i][j] == 1):
                area = traverse(i,j)
                areas = max(areas, area)

    print(areas)

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

maxAreaOfIsland(grid)
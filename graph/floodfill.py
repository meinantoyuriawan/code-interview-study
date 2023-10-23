from collections import deque

def floodfill(image, sr, sc, color):
    if not image:
        return
    
    start = image[sr][sc]

    image[sr][sc] = color
    
    rows, cols = len(image), len(image[0])
    visited = set()
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
                # 2. image element[i][j] == "1"
                # 3. i, j not in visited
                if ((i>=0 and i<rows) and 
                    (j>=0 and j<cols) and 
                    image[i][j] == start and 
                    (i, j) not in visited):
                    image[i][j] = color
                    q.append((i, j))
                    visited.add((i,j))

    traverse(sr, sc)
                
    return image

grid = [
  ["1","1","0"],
  ["1","1","0"],
  ["1","0","1"]
]

islands = floodfill(grid, 0, 0, "2")

print(islands)
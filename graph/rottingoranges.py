from collections import deque

def rottingoranges(grid):


    q = deque()
    time, fresh = 0,0

    rows, cols = len(grid), len(grid[0])

    if not grid:
        return -1
    
    # this problem is multi source bfs, basically we store every source and iterate the tranversal algorithm using source
    
    # 1. find fresh orange location
    # 2. find rotten orange location
    # q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 :
                fresh +=1
            if grid[r][c] == 2:
                q.append([r, c])

    directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    # the tranversal algorithm ends in the condition of q and fresh is not zero
    # q is the rotten oranges
    # fresh is fresh oranges, if it isnt reach zero, then that means it is impossible to all of the fresh orange is rotten
    while q and fresh > 0:

        # the loop starting from len(q), the amount of source. For every grid that affected from every responsible source, the len(q) resets
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row<0 or row == rows or
                    col<0 or col == cols or 
                    grid[row][col] != 1):
                    continue
                # the code below means if the condition unmet, set the grid to rotten and append it for next queue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1

    return time if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]

res = rottingoranges(grid)

print(res)
from collections import deque

def pacificAtlantic(heights):

    # return(pacificAtlanticBFS(heights))
    return(pacificAtlanticDFS(heights))

def pacificAtlanticBFS(heights):

    # on progress, doesnt know how to

    if not heights:
        return
    
    rows = len(heights)
    cols = len(heights[0])

    directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

    left = 0
    right = len(heights[0])
    top = 0
    bottom = len(heights)
    
    res = []
    # traverse

    def traverse(i,j):
        q = deque()
        visited = set()
        visited.add((i, j))
        q.append((i,j))
        p = 0
        a = 0

        while q:
            cur_i, cur_j = q.popleft()
            elems = heights[cur_i][cur_j]
            for di, dj in directions:
                i, j = cur_i + di, cur_j + dj
                # conditions
                # 1. check neighbors
                # 2. grid elements[i][j]<=grid elements[cur_i][cur_j]
                if ((i>=left and i<right) and (j>=top and j<bottom) and heights[i][j] <= elems and (i, j) not in visited):
                    q.append((i,j))
                    visited.add((i, j))

                    if ((i == left or j == top)):
                        p = 1
                        # print(cur_i, cur_j)
                        # print('reached pacific')
                    if ((i == right-1 or j == bottom-1)):
                        a = 1
                        # print(cur_i, cur_j)
                        # print('reached atlantic')
            if p ==1 and a ==1:
                res.append([cur_i, cur_j])

    for r in range(rows):
        for c in range(cols):
            traverse(r,c)

    return res

def pacificAtlanticDFS(heights):
    rows, cols = len(heights), len(heights[0])
    # create 2 set for each ocean, iterate in 2 direction (l->r, r->l) and (t->b, b->t)
    pacific, atlantic = set(), set()

    # dfs function for each element
    # the logic consist of comparing previous Height with current height
    # we send the current height for next dfs as a previous height in their pov

    def dfs(r, c, visit, prevHeight):
        if(
            (r, c) in visit or
            r<0 or c<0 or
            r== rows or c == cols or
            heights[r][c] < prevHeight
        ):
            return
        
        visit.add((r,c))
        dfs(r+1, c, visit, heights[r][c]) #down
        dfs(r-1, c, visit, heights[r][c]) #up
        dfs(r, c+1, visit, heights[r][c]) #right
        dfs(r, c-1, visit, heights[r][c]) #left

    for c in range(cols):
        # run dfs for every element in a column (r-l && l-r)
        dfs(0, c, pacific, heights[0][c])
        dfs(rows-1, c, atlantic, heights[rows-1][c])

    for r in range(rows):
        # run dfs for every element in a column (r-l && l-r)
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols-1, atlantic, heights[r][cols-1])

    # for every respective set (pacific and atlantic), both exist = the answer
    res = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in pacific and (r, c) in atlantic:
                res.append([r, c])
    
    return res
    

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacificAtlantic(matrix))
def combination(n, k):

    stack =[]
    res =[]
    def backtrack(start):
        if len(stack) == k:
            res.append(stack.copy())
            return
        
        for i in range(start, n+1):
            stack.append(i)
            backtrack(i+1)
            stack.pop()
    
    backtrack(1)

    return res

print(combination(4,2))
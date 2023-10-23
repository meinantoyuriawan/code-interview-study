def permutation(nums):
    # def backtrack(nums):
    res =[]
    if len(nums) == 1:
        return [nums.copy()]

    
    for i in range(len(nums)):
        n = nums.pop(0)

        perms = permutation(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    
    return res
    
    # backtrack(1)

    # return res

def anotherSolution(nums):
    res = []
    path = []
    used = [False] * len(nums)
    def dfs(path, used, res):
        if len(path) == len(nums):
            res.append(path.copy())
            return
        
        for i, num in enumerate(nums):
            if used[i]:
                continue
            
            path.append(num)
            used[i] = True
            dfs(path, used, res)

            path.pop()
            used[i] = False

    dfs(path, used, res)
    return res


nums = [1,2,3]
res = permutation(nums)
print(res)

res = anotherSolution(nums)
print(res)
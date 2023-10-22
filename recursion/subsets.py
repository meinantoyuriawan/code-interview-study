def subsets(nums):

    stack =[]
    res =[]

    # [1,2,3]
    def backtrack(i):
        if i >= len(nums):
            # print(stack)
            res.append(stack.copy())
            return
        
        # decision to include
        stack.append(nums[i])
        print(stack)
        backtrack(i+1)

        # decision to not inculde
        stack.pop()
        print(stack)
        backtrack(i+1)

    backtrack(0)
    return res

n = [1,2,3]
res = subsets(n)

print(res)
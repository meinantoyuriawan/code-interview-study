def SubsetsDup(nums):
    stack = []
    res = []
    nums.sort()

    def backtrack(i):
        if i == len(nums):
            res.append(stack.copy())
            return
    
        # all subs that include nums[i]
        stack.append(nums[i])
        backtrack(i+1)
        stack.pop()

        # all subs that dont include nums[i]
        # cond 1 == out of bounds
        # cond 2 == current and next element is equal
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        backtrack(i+1)

    backtrack(0)
    return res

n = [1,2,2,3]
res = SubsetsDup(n)

print(res)
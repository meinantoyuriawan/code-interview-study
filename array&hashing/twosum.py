def twoSum(nums, target):
    for i in range(len(nums)):
        temp = nums[i]
        for j in range(i+1, len(nums)):
            if (temp + nums[j]==target):
                return([i,j])
            
nums = [2, 7, 11, 15]
target = 9

twoSum(nums, target)
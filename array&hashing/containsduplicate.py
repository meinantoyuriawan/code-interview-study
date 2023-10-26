def containsDuplicate(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
        
nums = [1,2,3,1]
containsDuplicate(nums)
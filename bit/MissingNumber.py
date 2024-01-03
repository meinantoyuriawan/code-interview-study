def missingNumber(nums):
    # xor
    s = 0
    for i in nums:
        s=s^i
    for i in range(len(nums)+1):
        s=s^i
    
    return s

# Input: nums = [3,0,1]
# Output: 2

nums = [3,0,1]
print(missingNumber(nums))
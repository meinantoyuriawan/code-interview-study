def findMin(nums):
    # binary search
    # 1. find the mid element
    # 2. if mid > what to search, look in right half (positive trend)
    # 3. if mid < what to search, look in left half (negative trend)
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid +1
            else :
                right = mid
        return(nums[right])
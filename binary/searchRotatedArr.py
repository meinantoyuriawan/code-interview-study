# nums = [4,5,6,7,0,1,2], target = 0
# out = 4

def search(nums, target):
    l = 0
    r = len(nums)-1

    while l<=r:
        mid = (l+r)//2
        if nums[mid] ==target:
            return mid
        
        # 2 usecase
        # 1st [4567012] target 0
        # 4,7,2
        # l<mid
        # t<mid
        # go right (leftest element is the lowest and the target even lower than that)
        # (the trend is most likely positive until mid)
        # binary search as usual
        if nums[l] <= nums[mid]:
            if target < nums[l] or target > nums[mid]:
                # go right
                l = mid+1
            else:
                r = mid-1
        # 2nd [45123] target 2
        # 4,1,3
        # l>mid
        # t>mid
        # go right (the target is bigger than mid element)
        # (the trend is negative towards mid because l>mid)
        # binary search as usual
        else:
            if target<nums[mid] or target>nums[r]:
                # go left
                r = mid-1
            else:
                l = mid+1

    return -1

def run_testcase():
    nums = [[4,5,6,7,0,1,2],[4,5,6,7,0,1,2], [1]]
    target = [0, 3, 0]
    output = [4, -1, -1]
    for i in range(len(nums)):
        if (search(nums[i], target[i])) != output[i]:
            print("Testcase %s failed, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))
            continue
        print("Testcase %s success, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))

if __name__ == "__main__":
    run_testcase()
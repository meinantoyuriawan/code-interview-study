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


def run_testcase():

    s1 = [[3,4,5,1,2], [4,5,6,7,0,1,2], [11,13,15,17]]
    output = [1, 0, 11]
    for i in range(len(s1)):
        if (findMin(s1[i])) != output[i]:
            print("Testcase %s failed, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))
            continue
        print("Testcase %s success, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))

if __name__ == "__main__":
    run_testcase()
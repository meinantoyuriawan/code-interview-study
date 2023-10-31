def binarySearch(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = l + (r-l) //2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1

        elif nums[mid] > target:
            r = mid - 1

    return -1


def run_testcase():
    nums = [[-1,0,3,5,9,12],[-1,0,3,5,9,12]]
    target = [9, 2]
    output = [4, -1]
    for i in range(len(nums)):
        if (binarySearch(nums[i], target[i])) != output[i]:
            print("Testcase %s failed, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))
            continue
        print("Testcase %s success, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))

if __name__ == "__main__":
    run_testcase()
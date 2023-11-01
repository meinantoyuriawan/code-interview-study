def search2d(matrix, target):
    l = 0
    top = 0
    r = len(matrix[0]) -1
    bottom = len(matrix) -1

    # check if the target in between row

    while top <= bottom:
        row = (top + bottom )//2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    
    if not (top <= bottom):
        return False
    row = (top + bottom) // 2

    while l <= r:
        mid = (l+r)//2
        # if matrix[row][mid] == target:
        #     return True

        if matrix[row][mid] < target:
            l = mid + 1

        elif matrix[row][mid] > target:
            r = mid - 1
        else:
            return True

    return False


def run_testcase():
    nums = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]],[[1,3,5,7],[10,11,16,20],[23,30,34,60]]]
    target = [3, 13]
    output = [True, False]
    for i in range(len(nums)):
        if (search2d(nums[i], target[i])) != output[i]:
            print("Testcase %s failed, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))
            continue
        print("Testcase %s success, nums: %s, target: %s, outcome: %s" % (i+1, 
                nums[i], target[i], output[i]))

if __name__ == "__main__":
    run_testcase()
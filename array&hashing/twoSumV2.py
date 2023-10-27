def twoSum(nums, target):
    indexes = {}
    for i in range(0, len(nums)):
        second_operand = target - nums[i]
        if second_operand in indexes:
            return [indexes[second_operand], i]
        indexes[nums[i]] = i
    return indexes

# two pointer (in leetcode, the array is sorted for this particular problem)
def twoSum2Pointer(nums, target):
    l = 0
    r = len(nums) -1

    while l<r:
        if nums[l] + nums[r] == target:
            return ([l,r])
        elif nums[l] + nums[r] < target:
            l+=1
        else:
            r-=1

def run_testcase():
    input = [[2, 7, 11, 15], [3,2,4]]
    target = [9, 6]
    expected_output = [[0,1], [1,2]]
    for i in range(len(input)):
        if (twoSum(input[i], target[i]) != expected_output[i]):
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
def longestConsecutive(nums):
    nums.sort()
    count = 0
    temp = 1
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    for i in range(0, len(nums)-1):
        if (nums[i] + 1 == nums[i+1]):
            temp += 1
        elif nums[i] < nums[i+1]:
            temp = 1
        count = max(count, temp)
    return count


def run_testcase():
    input = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]
    expected_output = [4, 9]
    for i in range(len(input)):
        if (longestConsecutive(input[i]) != expected_output[i]):
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        
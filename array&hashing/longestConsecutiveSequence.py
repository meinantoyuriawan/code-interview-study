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

# my answer, it is the same with a little bit adjustment in same element and traverse start stop point
def longestConsec2(nums):
    count = min(1, len(nums))
    answer = 0
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if (nums[i] == nums[i-1] +1):
            count +=1
        elif (nums[i] == nums[i-1]):
            continue
        else:
            answer = max(count, answer)
            count = 1
    
    return max(answer, count)


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
        
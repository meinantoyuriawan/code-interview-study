def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = len(nums)-1

        while l<r:
            sums = nums[i] + nums[l] + nums[r]
            if sums <0:
                l +=1
            elif sums >0:
                r-=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res

def run_testcase():
    input = [[-1,0,1,2,-1,-4], [0,1,1], [0,0,0]]
    output = [[[-1,-1,2],[-1,0,1]], [], [[0,0,0]]]
    for i in range(len(input)):
        vals = threeSum(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
            
if __name__ == "__main__":
    run_testcase()
def trapRain(height):
    # the point of this is get minimum value between highest neighbor, maxL and maxR
    # the minimum value from before then can be reference for a maximum value of current element can hold
    l = 0
    r = len(height) -1
    res = 0
    # time limit
    # for i in range(1, len(height)-1):
    #     maxL = height[l]
    #     maxR = height[r]
    #     # find max l
    #     for j in range(l, i):
    #         if height[j] > maxL:
    #             # print(j)
    #             maxL = height[j]
    #     # find max r
    #     for k in range(r, i, -1):
    #         if height[k] > maxR:
    #             maxR = height[k]
    #     # print(maxL, maxR, h[i])
    #     vals = min(maxL, maxR) - height[i]
    #     if vals>0:
    #         res += vals

    # two pointer magic
    # traverse the height in 2 ways, left and right.
    # compare between 2 maxL and maxR, if one of them is less than another, set it as reference
    # move the pointer 1 step
    # get the maximum value between current pointer height with its respective neighbors, if the maximum value remains than it means it can hold value
    # if not then the maximum value is the current pointer, the result can't hold value (the eq will canceling)
    maxL = height[l]
    maxR = height[r]
    while l<r:
        if maxL<maxR:
            l+=1
            maxL = max(maxL, height[l])
            res += maxL-height[l]
        else:
            r-=1
            maxR = max(maxR, height[r])
            res += maxR-height[r]
    
    return res



def run_testcase():
    input = [[0,1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5]]
    output = [6, 9]
    for i in range(len(input)):
        vals = trapRain(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s, but instead: %s" % (i+1, 
                input[i], output[i], vals))
            
if __name__ == "__main__":
    run_testcase()
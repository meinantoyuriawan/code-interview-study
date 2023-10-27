def containerMost(height):
    l = 0
    r = len(height)-1

    maxVol = 0
    while l<r:
        h = min(height[l], height[r])
        vol = h * (r-l)
        maxVol = max(maxVol, vol)
        if height[l] > height[r]:
            r-=1
        else: 
            l+=1
    return maxVol


def run_testcase():
    input = [[1,8,6,2,5,4,8,3,7], [1,1]]
    output = [49, 1]
    for i in range(len(input)):
        vals = containerMost(input[i])
        if output[i] == vals:
            print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
        else:
            print("Testcase %s failed, input: %s, outcome: %s, but instead: %s" % (i+1, 
                input[i], output[i], vals))
            
if __name__ == "__main__":
    run_testcase()
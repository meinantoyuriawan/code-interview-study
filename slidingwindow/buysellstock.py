def maxProfit(prices):
    # set the pivot element for lowest prices in array
    # traverse through prices array
    # if the current element is less than pivot element, set the new pivot element as minimum
    # else, count the profit between current prices and pivot element
    # if the profit is greater than maximum profit from before, set the new profit as maximum profit
    maxprof = 0

    minimum = prices[0]

    for i in range(len(prices)):
        if(prices[i]<minimum):
            minimum = prices[i]
        else:
            temp = prices[i] - minimum
            if (temp>maxprof):
                maxprof = temp
    
    return maxprof

def run_testcase():

    s1 = [[7,1,5,3,6,4], [7,6,4,3,1]]
    output = [5, 0]
    for i in range(len(s1)):
        if (maxProfit(s1[i])) != output[i]:
            print("Testcase %s failed, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))
            continue
        print("Testcase %s success, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))

if __name__ == "__main__":
    run_testcase()
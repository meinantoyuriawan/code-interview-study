def maxProfit(prices):
    maxprof = 0

    minimum = prices[0]

    for i in range(len(prices)):
        if(prices[i]<minimum):
            minimum = prices[i]
        else:
            temp = prices[i] - min
            if (temp>maxprof):
                maxprof = temp
    
    return maxprof
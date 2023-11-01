import math

def minEatingSpeed(piles, h):
    # maxPiles = (sorted(piles))[-1]
    maxPiles = max(piles)
    def countHours(piles, k):
        countH = 0
        for i in range(len(piles)):
            countH += math.ceil(piles[i] / k)
        return countH
    
    l = 1
    r = maxPiles
    res = r

    while l<=r:
        mid = (l+r) //2

        hours = countHours(piles, mid)
        if hours <= h:
            res = min(res, mid)
            r = mid-1
        
        else:
            l = mid+1

    return res


print(minEatingSpeed([3,6,7,11], 8)) #k = 4
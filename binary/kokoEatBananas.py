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

# piles = [30,11,23,4,20], h = 5 k =30
# piles = [30,11,23,4,20], h = 6 k =23

# print(minEatingSpeed([3,6,7,11], 8)) #k = 4


def run_testcase():

    piles = [[3,6,7,11], [30,11,23,4,20], [30,11,23,4,20]]
    h = [8, 5, 6]
    output = [4, 30, 23]
    for i in range(len(piles)):
        if (minEatingSpeed(piles[i], h[i])) != output[i]:
            print("Testcase %s failed, piles: %s, h: %s, outcome: %s" % (i+1, 
                piles[i], h[i], output[i]))
            continue
        print("Testcase %s success, piles: %s, h: %s, outcome: %s" % (i+1, 
                piles[i], h[i], output[i]))

if __name__ == "__main__":
    run_testcase()
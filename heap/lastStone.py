import heapq

def lastStone(stones):
    while True:
        stack = []
        if len(stones) < 2:
            break
        heapq.heapify(stones)
        while len(stones) > 2:
            ele = heapq.heappop(stones)
            stack.append(ele)
        # compare two stones
        res = stones[1] - stones[0]
        stack.append(res)
        stones = stack
    return stones[0]

def lastStonesMaxHeap(stones):
    nStones = []
    for i in stones:
        nStones.append(i*-1)

    heapq.heapify(nStones)

    while len(nStones) > 1:
        # compare two stones
        first = heapq.heappop(nStones)
        second = heapq.heappop(nStones)
        if second>first:
            heapq.heappush(nStones, first-second)
    
    nStones.append(0) # for the stones length <=2
    return abs(nStones[0])

num = [2,7,4,1,8,1]
res = lastStone(num)
res2 = lastStonesMaxHeap(num)
print(res)
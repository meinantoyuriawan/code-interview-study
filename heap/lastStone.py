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

num = [2,7,4,1,8,1]
res = lastStone(num)
print(res)
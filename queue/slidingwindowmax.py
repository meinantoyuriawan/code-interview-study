# monotonic queue,always decreasing queue

from collections import deque

def maxSlidingWindow(nums, k):
    q = deque() # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            print("current tail", nums[q[-1]], "incoming", cur)
            print("will be poped", q)
            q.pop()
        q.append(i)
        print("appended", q)
        # remove first element if it's outside the window
        if q[0] == i - k:
            print("outside the window", q)
            q.popleft()
        # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            print("append", q[0])
            res.append(nums[q[0]])
    return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

res = maxSlidingWindow(nums, k)
print(res)
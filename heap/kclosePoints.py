import heapq

def kClosePoints(points, k):
    hashPoint = {}
    root = []
    res = []
    for i in points:
        x = i[0] * i[0]
        y = i[1] * i[1]
        sq = x+y
        if sq not in hashPoint:
            hashPoint[sq] = [i]
        else:
            hashPoint[sq].append(i)
        root.append(-sq)

    heapq.heapify(root)

    while len(root) > k:
        heapq.heappop(root)

    for i in root:
        if -i in hashPoint:
            ele = hashPoint[-i].pop()
            res.append(ele)
    return res

def merge(intervals):
    # sort the intervals

    for i in range(len(intervals)):
        for j in range(0, len(intervals)-i-1):
            if intervals[j][0] > intervals[j+1][0]:
                temp = intervals[j]
                intervals[j] = intervals[j+1]
                intervals[j+1] = temp

    res = [intervals[0]]

    for i in range(1, len(intervals), 1):
        if (intervals[i][0]) <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append([intervals[i][0], intervals[i][1]])

    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]

res = merge(intervals)

print(res)
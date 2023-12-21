def erase(intervals):

    # sort

    # for i in range(len(intervals)):
    #     for j in range(0, len(intervals)-i-1):
    #         if intervals[j][0] > intervals[j+1][0]:
    #             temp = intervals[j]
    #             intervals[j] = intervals[j+1]
    #             intervals[j+1] = temp

    intervals.sort()

    res = 0
    prevEnd = intervals[0][1]

    # find interlap, append the res. Set the new end as minimum of both prevend and current end

    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)

    return res

    
    

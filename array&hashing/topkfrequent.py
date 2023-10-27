def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hmap = {}
    for i in nums:
        if i not in hmap:
            hmap[i] = 1
        else:
            hmap[i] += 1

    # my early solution; 351ms, 16,5mb(good memory)
    # freq = {}
    # res = []
    # for j in hmap:
    #     res.append(hmap[j])
    #     if hmap[j] not in freq:
    #         freq[hmap[j]] = [j]
    #     else:
    #         freq[hmap[j]].append(j)
    # res = sorted(res)
    # print(freq)

    
    # ans = []
    # for x in range(k):
    #     ele = res[len(res)-x-1]
    #     for num in freq[ele]:
    #         if num not in ans:
    #             ans.append(num)
    # return ans

    # solution from neetcode; 98ms, 21,5mb(good run time)
    freq = [[] for _ in range(len(nums)+1)]

    for n,c in hmap.items():
        freq[c].append(n)
    ans = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            ans.append(n)
            if len(ans) == k:
                return ans

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
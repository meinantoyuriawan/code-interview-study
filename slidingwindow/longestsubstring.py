def lengthofLongestSubstring(s):
    temp = []
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in temp:
            temp.remove(s[l])
            l+=1
        temp.append(s[r])
        res = max(res, r-l+1)

    return res
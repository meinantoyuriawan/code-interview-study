def charReplacement(s, k):
    # mental model is (window len - max char in str)
    # shift right for every occurences that valid (windowlen - maxchar <= k)
    # if it is invalid, move left and count the maximum between current window and previous maximum window
    # stop when right is ended and is valid

    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        # store maximum char in hash
        if s[r] in count:
            count[s[r]] +=1
        else:
            count[s[r]] = 1

        # is valid
        if (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r-l+1)
    
    return res
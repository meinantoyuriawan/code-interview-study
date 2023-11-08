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


def run_testcase():

    s = ["ABAB", "AABABBA"]
    k = [2, 1]
    output = [4, 4]
    for i in range(len(s)):
        if (charReplacement(s[i], k[i])) != output[i]:
            print("Testcase %s failed, s: %s, k: %s, outcome: %s" % (i+1, 
                s[i], k[i], output[i]))
            continue
        print("Testcase %s success, s: %s, k: %s, outcome: %s" % (i+1, 
                s[i], k[i], output[i]))

if __name__ == "__main__":
    run_testcase()
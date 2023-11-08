def lengthofLongestSubstring(s):
    # traverse through s
    # if the current element is equal to the element in temp array, delete every element in leftest array, shift the left
    # count the maximum between the current window and before the count
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


def run_testcase():

    s1 = ['abcabcbb', "bbbbb", "pwwkew"]
    output = [3, 1, 3]
    for i in range(len(s1)):
        if (lengthofLongestSubstring(s1[i])) != output[i]:
            print("Testcase %s failed, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))
            continue
        print("Testcase %s success, s1: %s, outcome: %s" % (i+1, 
                s1[i], output[i]))

if __name__ == "__main__":
    run_testcase()
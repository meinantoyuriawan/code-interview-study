def checkInclusion(s1, s2):

    '''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.'''

    # steps
    # store every s1 element count in hash 1
    # set the window size as the length of s1
    # traverse through s2, store every element in hash 2
    # if the current iteration is equal to the window size, check the hash 2 and hash1, 
        # if it is equal return true
        # if it is not equal, shift the left window and pop every word in the left

    # if in every iteration there is no equal hashed element, return False
    # leetcode runtime 57ms, beats 92% python user (kinda good)

    h1 = {}
    for x in s1:
        if x in h1:
            h1[x] += 1
        else:
            h1[x] = 1

    l = 0
    window = len(s1)
    h2 = {}

    for r in range(len(s2)):
        if s2[r] in h2:
            h2[s2[r]] +=1
        else:
            h2[s2[r]] = 1

        if r-l+1 == window:
            if h2 == h1:
                return True
            else:
                h2[s2[l]] -=1
                if h2[s2[l]] == 0:
                    h2.pop(s2[l])
                l+=1

    return False


def run_testcase():

    s1 = ['ab', "ab"]
    s2 = ["eidbaooo", "eidboaoo"]
    output = [True, False]
    for i in range(len(s1)):
        if (checkInclusion(s1[i], s2[i])) != output[i]:
            print("Testcase %s failed, s1: %s, s2: %s, outcome: %s" % (i+1, 
                s1[i], s2[i], output[i]))
            continue
        print("Testcase %s success, s1: %s, s2: %s, outcome: %s" % (i+1, 
                s1[i], s2[i], output[i]))

if __name__ == "__main__":
    run_testcase()
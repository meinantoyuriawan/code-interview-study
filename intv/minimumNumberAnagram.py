def minSteps(s, t):
    count = 0
    map = {}
    if (len(s) != len(t)):
        return count
    for i in range(len(s)):
        ch = s[i]
        map[ch] = map.get(ch, 0) + 1
    for i in range(len(t)):
        ch = t[i]
        if map.get(ch,0) > 0:
            map[ch] -= 1
    for ch in map:
        if (map[ch] > 0):
            count += map[ch]
    return count

def run_testcase():
    input = [['bab', 'aba'], ['anagram', 'mangaar']]
    expected_output = [1, 0]
    for i in range(len(input)):
        if (minSteps(input[i][0], input[i][1]) != expected_output[i]):
            print("Testcase %s failed, input: %s, expected outcome: %s, outcome: %s" 
                % (i+1, input[i], expected_output[i], minSteps(input[i][0], input[i][1])))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
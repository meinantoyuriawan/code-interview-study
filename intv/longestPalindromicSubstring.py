def checkPalindrome(string):
    temp = ''
    for c in string:
        temp = c + temp
    if (temp == string):
        return True
    return False

def longestPalindrome(string):
    left = 0
    right = 0
    resLen = 0
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            length = j - i + 1
            if (length > resLen and checkPalindrome(string[i:j])):
                resLen = length
                left = i
                right = j
    return string[left:right]

def run_testcase():
    input = ['babad', 'abadi', 'peterpan']
    expected_output = ['bab', 'aba', 'ete']
    for i in range(len(input)):
        if (longestPalindrome(input[i]) != expected_output[i]):
            print("Testcase %s failed, input: %s, expected outcome: %s, outcome: %s" 
                % (i+1, input[i], expected_output[i], longestPalindrome(input[i])))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        
def isPalindrome(num):
    res = 0
    temp = num
    while (temp > 0):
        res = res*10 + temp % 10
        temp = temp // 10
    if (res == num):
        return True
    return False

def run_testcase():
    input = [121, 100, 22, 312]
    expected_output = [True, False, True, False]
    for i in range(len(input)):
        if (isPalindrome(input[i]) != expected_output[i]):
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        

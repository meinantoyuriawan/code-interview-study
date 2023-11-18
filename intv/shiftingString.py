def leftShift(string, d):
    temp = string[d:] + string[0:d]
    return temp

def rightShift(string, d):
    return leftShift(string, len(string) - d)

def shiftingString(string, left, right):
    result = leftShift(string, left)
    result = rightShift(result, right)
    return result

def run_testcase():
    input = [['abcdefg', 2, 4]]
    expected_output = ['fgabcde']
    for i in range(len(input)):
        if (shiftingString(input[i][0], input[i][1], input[i][2]) != expected_output[i]):
            print("Testcase %s failed, input: %s, expected outcome: %s, outcome: %s" 
                % (i+1, input[i], expected_output[i], shiftingString(input[i][0], input[i][1], input[i][2])))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        
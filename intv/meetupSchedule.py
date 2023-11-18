def countMap(hashMap, schedule):
    for num in schedule:
        if num not in hashMap:
            hashMap[num] = 1

def meetupSchedule(firstDay, lastDay):
    list_meet = []
    hashMap = {}
    countMap(hashMap, firstDay)
    countMap(hashMap, lastDay)
    for key in hashMap:
        list_meet.append(key)
    return len(list_meet)

def run_testcase():
    input = [[[1,2,3,3,3], [2,2,3,4,4]], [[1, 1, 2], [1, 2, 2]]]
    expected_output = [4, 2]
    for i in range(len(input)):
        if (meetupSchedule(input[i][0], input[i][1]) != expected_output[i]):
            print("Testcase %s failed, input: %s, expected outcome: %s, outcome: %s" 
                % (i+1, input[i], expected_output[i], longestPalindrome(input[i])))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        
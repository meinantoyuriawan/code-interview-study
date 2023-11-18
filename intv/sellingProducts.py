def countMap(hashMap, schedule):
    for num in schedule:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1

def sellingProducts(products, m):
    tmp_list = []
    hashMap = {}
    countMap(hashMap, products)
    for key in hashMap:
        tmp_list.append([hashMap[key], key])
    tmp_list = sorted(tmp_list)
    i = 0
    while (i < len(tmp_list)):
        if (tmp_list[i][0] <= m):
            m -= tmp_list[i][0]
            tmp_list[i][0] = 0
        if (tmp_list[i][0] == 0):
            tmp_list.remove(tmp_list[i])
            i -= 1
        i += 1
    return len(tmp_list)

def run_testcase():
    input = [[[1,1,1,2,3,2], 2], [[1, 1, 5,5], 2]]
    expected_output = [2, 1]
    for i in range(len(input)):
        if (sellingProducts(input[i][0], input[i][1]) != expected_output[i]):
            print("Testcase %s failed, input: %s, expected outcome: %s, outcome: %s" 
                % (i+1, input[i], expected_output[i], sellingProducts(input[i][0], input[i][1])))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], expected_output[i]))

if __name__ == "__main__":
    run_testcase()
        
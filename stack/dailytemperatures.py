# brute force approach
# def dailyTemp(temp):
#     stack = []
#     for t in range(len(temp)):
#         curr = temp[t]
#         count = 1
#         for n in range(t+1, len(temp)):
#             if temp[n] > curr:
#                 stack.append(count)
#                 break
#             elif n == len(temp)-1:
#                 stack.append(0)
#             else:
#                 count +=1
#     stack.append(0)
#     return stack

# 1. traverse through temp
# 2. if stack empty, append tuple element and index of the current iteration
# 3. while stack and current element is greater than the top element of stack
#   - pop stack, get the element and index
#   - calculate the current element index - stack pop index
#   - the difference is the amount index needed to get the stack pop index from current index
#   - store the data into array result
def dailyTemp(temp):
    res = [0] * len(temp)
    stack = []

    for ind, t in enumerate(temp):
        while stack and t > stack[-1][0]:
            _, stkInd = stack.pop()
            res[stkInd] = ind - stkInd
        stack.append((t, ind))
    
    return res


def run_testcase():
    input = [[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]]
    output = [[1,1,4,2,1,1,0,0], [1,1,1,0], [1,1,0]]
    for i in range(len(input)):
        if (dailyTemp(input[i])) != output[i]:
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))

if __name__ == "__main__":
    run_testcase()

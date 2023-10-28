def evalRPN(tokens):
    stack = []
    num = 0

    for t in tokens:
        if t in ["+", "*", "/", "-"]:
            val1 = int(stack.pop())
            val2 = int(stack.pop())

            if t == "+":
                vals = val1 + val2
                num = vals
            elif t == "*":
                vals = val2 * val1
                num = vals
            elif t == "-":
                vals = val2 - val1
                num = vals
            else:
                vals = val2/val1
                if -1< vals < 1:
                    vals = 0
                num = int(vals)
            stack.append(num)
        else:
            stack.append(int(t))

    return(stack[0])

def run_testcase():
    input = [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
    output = [9, 6, 22]
    for i in range(len(input)):
        if (evalRPN(input[i])) != output[i]:
            print("Testcase %s failed, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))
            continue
        print("Testcase %s success, input: %s, outcome: %s" % (i+1, 
                input[i], output[i]))

if __name__ == "__main__":
    run_testcase()
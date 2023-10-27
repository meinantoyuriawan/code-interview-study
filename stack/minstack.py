class MinStack(object):

    def __init__(self):
        self.A = []
        self.M = []

    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.M:
            self.M.append(val)
        else:
            self.M.append(min(val, self.M[-1]))
        return "null"

    def pop(self) -> None:
        self.A.pop()
        self.M.pop()
        return "null"

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.M[-1]
        
def run_testcase():
    input = ["MinStack",["push", -2],["push", 0],["push", -3],["getMin", 0],["pop", 0],["top", 0],["getMin", 0]]
    # [[],[-2],[0],[-3],[],[],[],[]]
    output = ["null","null","null","null",-3,"null",0,-2]

    obj = MinStack()
    for i in range(1, len(input)):
        if input[i][0] == "push":
            vals = obj.push(input[i][1])
            if vals == output[i]:
                print("push success ", vals)
            else :
                print("push failed, expected ", vals)
        elif input[i][0] == "pop":
            vals = obj.pop()
            if vals == output[i]:
                print("pop success ", vals)
            else :
                print("pop failed, expected ", vals)
        elif input[i][0] == "getMin":
            vals = obj.getMin()
            if vals == output[i]:
                print("getMin success ", vals)
            else :
                print("getMin failed, expected ", vals)
        elif input[i][0] == "top":
            vals = obj.top()
            if vals == output[i]:
                print("top success ", vals)
            else :
                print("top failed, expected ", vals)

        else:
            print('unknown command')
            
if __name__ == "__main__":
    run_testcase()

def carFleet(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def run_testcase():
    position = [[10,8,0,5,3], [3], [0,2,4]]
    speed = [[2,4,1,1,3], [3], [4,2,1]]
    target = [12, 10, 100]
    output = [3, 1, 1]
    for i in range(len(position)):
        if (carFleet(target[i], position[i], speed[i])) != output[i]:
            print("Testcase %s failed, position: %s, speed: %s, target: %s, outcome: %s" % (i+1, 
                position[i], speed[i], target[i], output[i]))
            continue
        print("Testcase %s success, position: %s, speed: %s, target: %s, outcome: %s" % (i+1, 
                position[i], speed[i], target[i], output[i]))

if __name__ == "__main__":
    run_testcase()
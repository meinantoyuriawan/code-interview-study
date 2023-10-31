def carFleet(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        print(stack)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(12,position, speed))
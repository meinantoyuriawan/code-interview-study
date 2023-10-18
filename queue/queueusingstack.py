class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        get every (except 1st) element from in_stack, append the element to out_stack in reverse order (from in_stack)
        pop the 1st element of in_stack as a result
        put back every element in out_stack to in_stack in reverse order (from out_stack or the same as in_stack before)
        """
        n = len(self.in_stack) -1
        for _ in range(n):
            self.out_stack.append(self.in_stack.pop())
        res = self.in_stack.pop()
        for _ in range(n):
            self.in_stack.append(self.out_stack.pop())
        return res

    def peek(self):
        """
        :rtype: int
        get every (except 1st) element from in_stack, append the element to out_stack in reverse order (from in_stack)
        get the 1st element of in_stack as a result
        put back every element in out_stack to in_stack in reverse order (from out_stack or the same as in_stack before)
        """
        n = len(self.in_stack) -1
        for _ in range(n):
            self.out_stack.append(self.in_stack.pop())
        res = self.in_stack[0]
        for _ in range(n):
            self.in_stack.append(self.out_stack.pop())
        return res
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.in_stack) == 0
        
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
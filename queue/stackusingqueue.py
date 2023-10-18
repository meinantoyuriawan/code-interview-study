import collections


class MyStack(object):

    def __init__(self):
        self._queue = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q = self._queue
        q.append(x)
        # for stack with left orientation
        # for _ in range(len(q) - 1):
        #     q.append(q.popleft())
        # or q.rotate(1)

    def pop(self):
        """
        :rtype: int
        """
        return self._queue.pop()
        # for stack with left orientation
        # return self._queue.popleft()

        

    def top(self):
        """
        :rtype: int
        """
        return self._queue[len(self._queue)-1]
        # for stack with left orientation
        # return self._queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._queue) == 0
    

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
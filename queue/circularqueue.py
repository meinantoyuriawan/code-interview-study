class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        # number of elements in q
        self.elem = 0
        # queue size
        self.size = k
        # index of head
        self.headIndex = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[(self.elem+self.headIndex)%self.size] =value

        self.elem +=1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.headIndex = (self.headIndex+1)%self.size
        self.elem -=1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.headIndex + self.elem-1)%self.size]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.elem == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.elem == self.size
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
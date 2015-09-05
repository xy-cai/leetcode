class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta1 = []
        self.sta2 = []
        self.top1 = -1
        self.top2 = -1
        
    
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.top1 += 1
        self.sta1.append(x)
        
    
    def pop(self):
        """
        :rtype: nothing
        """
        i = 0
        self.top2 = -1
        while self.top1!=-1: 
            self.top2 += 1
            self.sta2.append(self.sta1[self.top1])
            self.sta1.pop()
            self.top1 -= 1

        self.sta2.pop()
        self.top2 -= 1
        while self.top2!=-1:
            self.top1 += 1
            self.sta1.append(self.sta2[self.top2])
            self.sta2.pop()
            self.top2 -= 1
    
    def peek(self):
        """
        :rtype: int
        """
        i = 0
        self.top2 = -1
        while self.top1!=-1: 
            self.top2 += 1
            self.sta2.append(self.sta1[self.top1])
            self.sta1.pop()
            self.top1 -= 1
        ret = self.sta2[self.top2]
        while self.top2!=-1:
            self.top1 += 1
            self.sta1.append(self.sta2[self.top2])
            self.sta2.pop()
            self.top2 -= 1
        return ret
    
    def empty(self):
        """
        :rtype: bool
        """
        if self.top1 != -1:
            return False
        return True
x = Queue()
x.push(1)
x.push(2)
print x.peek()
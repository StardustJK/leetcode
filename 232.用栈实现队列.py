#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]



    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.s2:
            return self.s2.pop()
        while(self.s1):
            self.s2.append(self.s1.pop())
        return self.s2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.s2:
            return self.s2[-1]
        while(self.s1):
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.s1)&(not self.s2)



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

# @lc code=end


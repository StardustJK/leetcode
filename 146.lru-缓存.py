#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存
#

# @lc code=start
import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue=collections.deque()
        self.dict={}
        self.capacity=capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
                # 更新queue
            self.queue.remove(key)
            self.queue.append(key)
            self.dict[key]=value
        else:
            self.queue.append(key)
            self.dict[key]=value


        if len(self.queue)>self.capacity:
            x=self.queue.popleft()
            del self.dict[x]

        
            
        


        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

obj=LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))

obj.put(1,1)
obj.put(4,1)

print(obj.get(2))




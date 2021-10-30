#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        s=0
        while(i!=j):
            if(height[i]<=height[j]):
                s=max(height[i]*(j-i),s)
                i+=1
            else:
                s=max(height[j]*(j-i),s)
                j-=1

        return s
# @lc code=end
obj=Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))

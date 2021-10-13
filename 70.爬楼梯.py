#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=[1,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        
        return f[n]


# @lc code=end


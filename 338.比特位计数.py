#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums=[0]*(n+1)
        for i in range(1,n+1):
            if(i%2==0):
                nums[i]=nums[i/2]
            else:
                nums[i]=nums[i-1]+1

        return nums

# @lc code=end

obj=Solution()
obj.countBits(2)


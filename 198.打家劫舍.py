#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        [2,7,9,3,1]
        :rtype: int
    
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        

        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])

        return dp[i-1]
# @lc code=end


#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=nums[0]
        sum=0
        for i in range(len(nums)):
            sum=max(sum+nums[i],nums[i])
            maxSum=max(maxSum,sum)
        return maxSum



    
# @lc code=end



#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            nums[(nums[i]-1)%n]+=n

        result=[]
        for i in range(n):
            if nums[i]<=n:
                result.append(i+1)
        return result

# @lc code=end


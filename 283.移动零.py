#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start=0
        for i in range(len(nums)):
            if nums[i]==0:
                start=i
                break
        left=right=start
        for i in range(start,len(nums)):
            if nums[right]==0:
                right+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1


# @lc code=end
obj=Solution()
obj.moveZeroes([0,1,3,12,0])

#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow=nums[0]
        fast=nums[nums[0]]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[nums[fast]]
        
        finder=0
        while(finder!=slow):
            slow=nums[slow]
            finder=nums[finder]

        return finder
# @lc code=end
obj=Solution()
res=obj.findDuplicate([1,3,4,2,2])
print(res)

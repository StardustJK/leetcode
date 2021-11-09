#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        nums.sort()
        nums.reverse()
        return nums[k-1]
        
                 


# @lc code=end

solu=Solution()
print(solu.findKthLargest([3,2,3,1,2,4,5,5,6],4))
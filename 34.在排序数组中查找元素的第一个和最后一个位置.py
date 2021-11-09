#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


       
        def binarySearch(nums,target):
            left=0
            right=len(nums)

            while left<right:
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            return left

        leftindex=binarySearch(nums,target)
        rightindex=binarySearch(nums,target+1)-1

        if leftindex==len(nums) or nums[leftindex]!=target:
            return [-1,-1]
        else:
            return [leftindex,rightindex]

            
        
# @lc code=end

solu=Solution()

print(solu.searchRange([1],1))


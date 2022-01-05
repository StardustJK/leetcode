#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1


        while(left<=right):
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            # 右侧有序
            if nums[mid]<nums[right]:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
                    
            # 左侧有序
            else:
                if target<nums[mid] and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1

        return -1




# @lc code=end


#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        imax=nums[0]
        imin=nums[0]
        ans=nums[0]
        for i in range(1,n):
            mx=imax
            mn=imin
            imax=max(mx*nums[i],nums[i],mn*nums[i])
            imin=min(mx*nums[i],nums[i],mn*nums[i])
            ans=max(imax,ans)
        return ans

# @lc code=end

obj=Solution()
ans=obj.maxProduct([-4,-3,-2])
print(ans)


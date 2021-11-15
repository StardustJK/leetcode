#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        L=[1]*n
        R=[1]*n
        for i in range(1,n):
            L[i]=L[i-1]*nums[i-1]
            R[n-i-1]=R[n-i]*nums[n-i]

        ans=[0]*n
        for i in range(n):
            ans[i]=L[i]*R[i]
        return ans


# @lc code=end
solu=Solution()
solu.productExceptSelf([1,2,3,4])


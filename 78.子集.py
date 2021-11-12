#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]

        for i in nums:
            l =len(res)
            for j in range(l):
                res.append(res[j]+[i])
        return res
# @lc code=end

obj=Solution()
print(obj.subsets([1,2,3]))


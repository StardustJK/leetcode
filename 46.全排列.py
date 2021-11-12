#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n=len(nums)
        def dfs(nums,path,res,depth,index):
            if depth==n:
                res.append(path)
                return
            for i in range(n):
                if i not in index:
                    dfs(nums,path+[nums[i]],res,depth+1,index+[i])

        path=[]
        res=[]
        dfs(nums,path,res,0,[])
        return res
# @lc code=end


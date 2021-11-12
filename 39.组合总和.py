#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,target,res,path,index):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for i in range(index,len(candidates)):
                dfs(candidates,target-candidates[i],res,path+[candidates[i]],i)

        
        res=[]
        path=[]
        dfs(candidates,target,res,path,0)
        return res
# @lc code=end


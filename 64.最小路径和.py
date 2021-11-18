#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        for i in range(1,n):
            grid[0][i]+=grid[0][i-1]
        
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])

        return grid[m-1][n-1]
# @lc code=end

solu=Solution()
print(solu.minPathSum([[1,2,3],[4,5,6]]))


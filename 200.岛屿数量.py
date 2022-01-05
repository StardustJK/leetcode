#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    res+=1
        
        return res
    
    def dfs(self,grid,i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
            return
        if grid[i][j]!='1':
            return
        
        grid[i][j]=2
        
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        
# @lc code=end


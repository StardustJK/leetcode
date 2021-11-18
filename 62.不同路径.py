#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        # """
        s=numpy.ones((m,n),dtype=int)


        for i in range(1,m):
            for j in range(1,n):
                s[i][j]=s[i-1][j]+s[i][j-1]

        return s[m-1][n-1]
        # return math.comb(m + n - 2, n - 1)

# @lc code=end
suol=Solution()
print(suol.uniquePaths(3,7))


#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]
        dp[0].append("")
        for i in range(n+1):
            for p in range(i):
                q=i-1-p
                for kp in dp[p]:
                    for kq in dp[q]:
                        dp[i].append("("+kp+")"+kq)

        return dp[n]
# @lc code=end
solu=Solution()
re=solu.generateParenthesis(3)
print(re)
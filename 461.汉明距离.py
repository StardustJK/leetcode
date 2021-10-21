#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        out=x^y
        out2=str(bin(out))
        count=0
        for i in out2:
            if i=='1':
                count+=1

        return count



# @lc code=end


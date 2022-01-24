#
# @lc app=leetcode.cn id=406 lang=python
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key=lambda x:(-x[0],x[1]))

        res=[]
        for p in people:
            if p[1]>=len(res):
                res.append(p)
            else:
                res.insert(p[1],p)

        return res

# @lc code=end


#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        a = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        res=[]
        i=0
        for k1,v in a:
            if(i==k):
                break
            res.append(k1)
            i+=1
        return res

# @lc code=end
obj=Solution()
obj.topKFrequent([1,1,1,2,2,3],2)

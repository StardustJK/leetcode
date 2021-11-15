#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp=collections.defaultdict(list)
        for str in strs:
            mp["".join(sorted(str))].append(str)
        
        return list(mp.values())

# @lc code=end


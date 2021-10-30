#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxCount=0
        list=[]
        for i in range(len(s)):
            if s[i] not in list:
                list.append(s[i])
                maxCount=max(maxCount,len(list))
            else:
                while (s[i] in list):
                    list.pop(0)
                list.append(s[i])
        return maxCount
# @lc code=end

obj=Solution()
len=obj.lengthOfLongestSubstring("aabaab!bb")
print(len)

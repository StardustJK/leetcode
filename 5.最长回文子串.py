#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=end=0
        maxlen=0
        for i in range(len(s)):
            odd=self.centerSpread(s,i,i+1)
            even=self.centerSpread(s,i,i)
            if (odd[1])>maxlen:
                start=odd[0]
                end=odd[0]+odd[1]
                maxlen=odd[1]
            if (even[1])>maxlen:
                start=even[0]
                end=even[0]+even[1]
                maxlen=even[1]

        return s[start:end]

    
    def centerSpread(self,s,left,right):
        while(left>=0 and right<len(s)):
            if(s[left]==s[right]):
                left-=1
                right+=1
            else:
                break

        
        return [left+1,right-left-1]

# @lc code=end

obj=Solution()
print(obj.longestPalindrome("a"))
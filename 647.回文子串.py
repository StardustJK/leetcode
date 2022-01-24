#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0

        for i in range(len(s)):
            ans+=1
            left=i-1
            right=i+1
            while(left>=0 and right<len(s)):
                if(s[left]==s[right]):
                    ans+=1
                    left-=1
                    right+=1
                else:
                    break
            
            if(i+1<len(s) and s[i]==s[i+1]):
                left=i-1
                right=i+1

                while(left>=0 and right<len(s)):
                    if(s[left]==s[right]):
                        ans+=1
                        left-=1
                        right+=1
                    else:
                        break
        
        return ans
            
# @lc code=end
obj=Solution()
print(obj.countSubstrings("aaa"))

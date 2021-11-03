#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
            }

        if(len(digits)==0):
            return []

        res=[]
        def backtrace(conbination,nextDigit):
            if(len(nextDigit)==0):
                res.append(conbination)
            else:
                for letter in dic[nextDigit[0]]:
                    backtrace(conbination+letter,nextDigit[1:])

        backtrace('',digits)
        return res

# @lc code=end


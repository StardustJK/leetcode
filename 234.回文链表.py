#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count=0
        p=head
        while(p):
            count+=1
            p=p.next

        pos=count/2
        
        left=right=head
        for i in range(pos):
            right=right.next
        if count%2!=0:
            right=right.next

        pre=next=None
        while(right):
            next=right.next
            right.next=pre
            pre=right
            right=next
    
        right=pre

        while(right):
            if(right.val!=left.val):
                return False
            left=left.next
            right=right.next
        
        return True
# @lc code=end


#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode()
        pre=prehead
        while(l1 and l2):
            if l1.val<=l2.val:
                pre.next=l1
                l1=l1.next

            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next

        if l1 is None:
            pre.next=l2
        if l2 is None:
            pre.next=l1
        return prehead.next


        
           
# @lc code=end


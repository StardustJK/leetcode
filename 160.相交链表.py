#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA=0
        countB=0
        pa=headA
        pb=headB

        while(pa):
            countA+=1
            pa=pa.next
        
        while(pb):
            countB+=1
            pb=pb.next

        pa=headA
        pb=headB

        if countA>=countB:
            step=countA-countB
            for i in range(step):
                pa=pa.next

            while(pa):
                if pa==pb:
                    return pa
                pa=pa.next
                pb=pb.next

            return None

        if countB>countA:
            step=countB-countA
            for i in range(step):
                pb=pb.next

            while(pa):
                if pa==pb:
                    return pa
                pa=pa.next
                pb=pb.next
                
            return None


            
# @lc code=end


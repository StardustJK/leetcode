#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        # 划分

        slow=head
        fast=head.next

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)

        h=ListNode(0)
        res=h 

        # 归并
        while(left and right):
            if left.val<=right.val:
                h.next=left
                left=left.next
            
            else:
                h.next=right
                right=right.next
            
            h=h.next
                            
        if left:
            h.next=left
        if right:
            h.next=right

        return res.next
        
        
        
        
# @lc code=end

node1=ListNode(3)
node2=ListNode(1,node1)
node3=ListNode(2,node2)
node4=ListNode(4,node3)

solu=Solution()
res=solu.sortList(node4)
print(res)

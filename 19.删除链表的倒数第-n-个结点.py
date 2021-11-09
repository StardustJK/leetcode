#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy=ListNode()
        dummy.next=head
        pre=dummy
        p=q=head
        for i in range(n):
            q=q.next

        while(q):
            pre=pre.next
            q=q.next
            p=p.next

        pre.next=p.next
        return dummy.next

# @lc code=end
node1=ListNode(1)
solu=Solution()
re=solu.removeNthFromEnd(node1,1)
print(re)


#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q=collections.deque()
        q.append(root.left)
        q.append(root.right)
        while q :
            left=q.popleft()
            right=q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if(left.val!=right.val):
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True
            
        

# @lc code=end
node1=TreeNode()
node1.val=1
node2=TreeNode()
node2.val=2
node3=TreeNode()
node3.val=2
node4=TreeNode()
node4.val=3
node5=TreeNode()
node5.val=4
node6=TreeNode()
node6.val=4
node7=TreeNode()
node7.val=3
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
obj=Solution()
obj.isSymmetric(node1)

#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1
        if not root1 and not root2:
            return None
        root1.val+=root2.val
        self.merge(root1,root2)
        return root1
        
    def merge(self,root1,root2):
        if not root1 or not root2:
            return
        if root1.left and root2.left:
            root1.left.val+=root2.left.val
        elif not root1.left and root2.left:
            node=TreeNode()
            node.val=root2.left.val
            root1.left=node
        

        if root1.right and root2.right:
            root1.right.val+=root2.right.val
        elif not root1.right and root2.right:
            node=TreeNode()
            node.val=root2.right.val
            root1.right=node

        self.merge(root1.left,root2.left)
        self.merge(root1.right,root2.right)
        
        
        
# @lc code=end
node5=TreeNode()
node5.val=3
node6=TreeNode()
node6.val=3
node3=TreeNode()
node3.val=2
node3.left=node5
node4=TreeNode()
node4.val=2
node4.right=node6
node1=TreeNode()
node1.val=1
node1.left=node3
node2=TreeNode()
node2.val=1
node2.right=node4
obg=Solution()
obg.mergeTrees(node1,node2)


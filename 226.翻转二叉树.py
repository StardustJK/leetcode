#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.invert(root)
        return root
        
        
    def invert(self,node):
        if  node:
            node.left,node.right=node.right,node.left
            self.invert(node.left)
            self.invert(node.right)
        


# @lc code=end


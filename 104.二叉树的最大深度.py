#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursion(root,0)


    def recursion(self,node,depth):
        if not node:
            return depth
            
        else:
            return max(self.recursion(node.left,depth+1),self.recursion(node.right,depth+1))

# @lc code=end


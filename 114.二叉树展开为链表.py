#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        list=[root]
        pre=TreeNode()
        head=pre
        while(list):
            temp=list.pop()
            if temp.right:
                list.append(temp.right)
            if temp.left:
                list.append(temp.left)
            pre.left=None
            pre.right=temp
            pre=pre.right



        return head.right


# @lc code=end


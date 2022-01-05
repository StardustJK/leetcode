#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        dict={}
        for i in range(len(inorder)):
            dict[inorder[i]]=i

        def buildMyTree(pre_left,pre_right,in_left,in_right):
            if pre_left>pre_right:
                return
            root_val=preorder[pre_left]
            root=TreeNode(val=root_val)

            in_root=dict[root_val]
            leftsize=in_root-in_left
            root.left=buildMyTree(pre_left+1,pre_left+leftsize,in_left,in_root-1)
            root.right=buildMyTree(pre_left+1+leftsize,pre_right,in_root+1,in_right)
            
            return root

        return buildMyTree(0,len(preorder)-1,0,len(preorder)-1)

# @lc code=end

solu=Solution()
root=solu.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(root)
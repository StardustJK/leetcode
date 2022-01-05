#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self) :
        self.sum=0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        head=root
        def dfs(root):
            if not root:
                return 
            dfs(root.right)
            self.sum+=root.val
            root.val=self.sum
            print(root.val)
            dfs(root.left)

        dfs(root)  
        return head
        
# @lc code=end
node1=TreeNode(1)
node2=TreeNode(0)
node3=TreeNode(2)
node1.left=node2
node1.right=node3
solu=Solution()
res=solu.convertBST(node1)
print(res)
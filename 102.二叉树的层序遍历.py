#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=collections.deque()
        queue.append(root)
        while(queue):
            n=len(queue)
            temp=[]
            for _ in range(n):
                pop=queue.popleft()
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                temp.append(pop.val)

            res.append(temp)
        return res
            
# @lc code=end

node1=TreeNode()
node1.val=3
node2=TreeNode()
node2.val=9
node3=TreeNode()
node3.val=20
node4=TreeNode()
node4.val=15
node5=TreeNode()
node5.val=7
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5
solu=Solution()
res=solu.levelOrder(node1)
print(res)

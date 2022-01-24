#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        courses=[0]*numCourses
        adjacency=[[] for _ in range(numCourses)]

        for pre,cur in prerequisites:
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not self.dfs(i,courses,adjacency):
                return False
        
        return True
        

# 0 表示没访问  -1 表示被其他节点访问了  1表示当前这轮被第二次访问
    def dfs(self,i,courses,adjacency):
        if courses[i]==-1:
            return True
        
        if courses[i]==1:
            return False
        
        courses[i]=1

        for j in adjacency[i]:
            if not self.dfs(j,courses,adjacency):
                return False
        courses[i]=-1
        return True



        
        
        

# @lc code=end


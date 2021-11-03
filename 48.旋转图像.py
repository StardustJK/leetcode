#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """


        layer=0
        m=n=0
        p=q=len(matrix)-1
        move=len(matrix)
        while(layer<len(matrix)/2):
            for i in range(move-1):
                matrix[m][n+i],matrix[m+i][q]=matrix[m+i][q],matrix[m][n+i]
                matrix[m][n+i],matrix[p][q-i]=matrix[p][q-i],matrix[m][n+i]
                matrix[m][n+i],matrix[p-i][n]=matrix[p-i][n],matrix[m][n+i]

            m+=1
            n+=1
            p-=1
            q-=1
            move-=2
            layer+=1
        return matrix

   
# @lc code=end

solu=Solution()
print(solu.rotate([[1,2,3,4,17,18],[5,6,7,8,19,20],[9,10,11,12,21,22],[13,14,15,16,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]))
# print(solu.rotate([[1,2,3],[4,5,6],[7,8,9]]))
# RIGHT
# [[31,25,13,9,5,1],
# [32,26,14,10,6,2],
# [33,27,15,11,7,3],
# [34,28,16,12,8,4],
# [35,29,23,21,19,17],
# [36,30,24,22,20,18]]
# WRONG
# [[31,25,13,9,5,1],[32,26,28,10,6,2],[33,27,11,12,14,3],[34,21,15,16,8,4],[35,29,23,7,19,17],[36,30,24,22,20,18]]

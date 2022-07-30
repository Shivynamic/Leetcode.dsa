def matrix(mat):
    for i in range(len(mat)):
            for j in range(i):
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
    for x in mat:
        x.reverse()
    
    
    
    
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        a = 4
        while a:
            matrix(mat)
            if mat == target:
                return True
            a-=1
        return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # '''
        m = len(matrix)
        n = len(matrix[0])
        if m==0:
            return False
        x,y = m-1,0
        while True:
            if x<0 or y>=n:
                break
            if matrix[x][y] > target:
                x-=1
            elif matrix[x][y]< target:
                y+=1
            else:
                return True
        return False
            
        # '''
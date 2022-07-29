class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        row = set()
        col =set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        
        row = list(row)
        col = list(col)
        row.sort()
        col.sort()
        
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j]=0
        '''
        
        row ,col = len(matrix),len(matrix[0])
        row_ze = False
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        row_ze = True
        
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
        if matrix[0][0]==0:
            for i in range(row):
                matrix[i][0]=0
        
        if row_ze:
            for j in range(col):
                matrix[0][j]=0
            
        
        
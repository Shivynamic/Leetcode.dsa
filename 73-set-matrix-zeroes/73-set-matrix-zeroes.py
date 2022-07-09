class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        col,row=False,False
        
    #check if first row and col has zero 
    
        for i in range(n):
            if matrix[i][0]==0:col=True
        for i in range(m):
            if matrix[0][i]==0:row=True
                
    #if position has zero set first col and first row zero for that 
    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0
                    
    #for every zero in first col set zero for every postion on that row
    
        for i in range(1,n):
            if matrix[i][0]==0:
                for j in range(1,m):
                    matrix[i][j]=0
                
    #for every zero in first row set zero for every postion on that col
    
        for j in range(1,m):
            if matrix[0][j]==0:
                for i in range(1,n):
                     matrix[i][j]=0
                        
    # if any of the check is true change all postions to zero

        if col:
            for i in range(n):
                matrix[i][0]=0

        if row:
            for j in range(m):
                matrix[0][j]=0
                
        
        
        
#         row = []
#         col = []
#         for i in range(len(matrix)):
#             if 0 in matrix[i]:
#                 row.append(i)
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==0:
#                     col.append(j)

#         col = list(set(col))
        
#         for k in row:
#             for j in range(len(matrix[0])):
#                 matrix[k][j]=0
#         for n in col:
#             for i in range(len(matrix)):
#                 matrix[i][n]=0
        
                
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
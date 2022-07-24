class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
			# Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        # Start adaptive search from bottom left corner
        y, x = h-1, 0
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target < current:
                # target is smaller, then go up
                y -= 1
            
            elif target > current:
                # target is larger, then go right
                x += 1
            
            else:
                # hit target
                return True
            
        return False
        '''
        m = len(matrix)
        n = len(matrix[0])
        if m==0:
            return False
        
        x,y = m-1,0
        while True:
            
            if x<0 or y>=m:
                break
            if matrix[x][y]==target:
                return True
            elif matrix[x][y] > target:
                x-=1
            else:
                y+=1
        return False
        '''
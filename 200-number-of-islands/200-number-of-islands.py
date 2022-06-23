import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row,col = len(grid),len(grid[0])
        
        xp = [-1,1,0,0]
        yp = [0,0,-1,1]
        
        def bfs(i,j):
            que = collections.deque()
            que.append((i,j))
            
            grid[i][j]="-1"
            
            while que:
                i,j = que.popleft()
                for k in range(4):
                    x = i+xp[k]
                    y = j+ yp[k]
                    
                    if x>=0 and x< row and y>=0 and y<col and grid[x][y]=="1":
                        grid[x][y]="-1"
                        que.append((x,y))
            
                        
        count =0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    bfs(i,j)
                    # print("HI")
                    count+=1
        return count
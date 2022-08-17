class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        coll = set()
        sumD = set()
        diffD = set()
        
        output=[]
        
        def solve(r):
            if r==n:
                res = ["".join(i) for i in board]
                output.append(res)
                return 
            
            for c in range(n):
                if c in coll or r+c in sumD or r-c in diffD:
                    continue
                
                coll.add(c)
                sumD.add(r+c)
                diffD.add(r-c)
                
                board[r][c] = "Q"
                solve(r+1)
                
                coll.remove(c)
                sumD.remove(r+c)
                diffD.remove(r-c)
                board[r][c] = "."
        solve(0)
        return output
        
        
        
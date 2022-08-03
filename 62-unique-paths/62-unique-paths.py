class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        N = m+n-2
        r = m-1
        res =1
        
        for i in range(1,r+1):
            res = res*(N-r+i)//i
            
        return res    
        '''dp = [[0]*n]*m
        
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        '''
        
        '''
        wrongg
        dp = [[-1]*n]*m
        print(dp)
        def help(i,j,m,n,dp):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j] = help(i+1,j,m,n,dp)+help(i,j+1,m,n,dp)
            return dp[i][j]
        return help(0,0,m,n,dp)'''
        
        
'''
        row = [1]*n
        for i in range(m-1):
            newRow= [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]
'''
        
        
        
'''
        def helper(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j >=n:
                return 0
            return helper(i+1,j,m,n)+helper(i,j+1,m,n)
        return helper(0,0,m,n)
        '''
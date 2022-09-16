class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N= len(nums)
        M= len(multipliers)
        
        INF = 10**20
        
        dp =[[-INF] * (M+1) for _ in range(M+1)]
        
        for n in range(M):
            for left in range(n+1):
                if n==0:
                    dp[n][left] =0 
                right = N+left - n -1
                
                score = dp[left][n] + nums[left] * multipliers[n]
                if score>dp[left+1][n+1]:
                    dp[left+1][n+1]=score
                
                score = dp[left][n] + nums[right] * multipliers[n]
                if score>dp[left][n+1]:
                    dp[left][n+1] = score
        
        return max(dp[i][M] for i in range(M+1))
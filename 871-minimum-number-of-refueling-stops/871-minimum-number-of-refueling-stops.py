class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n= len(stations)
        dp =[-1]*(n+1)
        dp[0] = startFuel
        
        for i in range(n):
            for ref in range(i,-1,-1):
                if dp[ref]>=stations[i][0]:
                    ref+=1
                    dp[ref] = max(dp[ref],dp[ref-1]+stations[i][1])
        
        for i in range(n+1):
            if dp[i]>=target:
                return i
        return -1
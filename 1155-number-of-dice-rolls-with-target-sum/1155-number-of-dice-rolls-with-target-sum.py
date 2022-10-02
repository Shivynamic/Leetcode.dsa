class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Edge case: target is impossible if too low or too high
        if n > target or target > n * k:
            return 0
        
        # Initialize memoization dictionary
        # key : value = sum of dice rolled : frequency of that sum occuring
        dp = {0:1}
        
        # Roll n dice
        for i in range(n):
            newDict = {}
            
            # Iterate over sums in memoization dictionary
            for prevSum in dp:
                # Iterate over all possible die rolls
                for j in range(1, k+1):
                    # For new updated sum, add the freq of the prevSum
                    if prevSum + j in newDict:
                        newDict[prevSum+j] += dp[prevSum]
                    else:
                        newDict[prevSum+j] = dp[prevSum]
                        
            # Replace memoization dictionary
            dp = newDict
            
        return dp[target] % (10**9 + 7)
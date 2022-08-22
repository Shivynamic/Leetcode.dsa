class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*len(s)
        for i in range(len(dp)):
            for j in range(i+1):
                w2check = s[j:i+1]
                if w2check in wordDict:
                    if j>0:
                        dp[i]+=dp[j-1]
                    else:
                        dp[i]+=1
        return dp[-1]>0
        
        
        
        
        '''dp = [False]*(len(s)+1)
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        '''
        
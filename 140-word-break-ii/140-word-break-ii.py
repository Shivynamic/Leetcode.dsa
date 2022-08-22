class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        
        def helper(s,ans):
            if len(s)==0:
                output.append(ans[:len(ans)-1])
                return 
            
            for i in range(len(s)):
                left = s[:i+1]
                if left in wordDict:
                    right = s[i+1:]
                    helper(right,ans+left+" ")
        helper(s,"")
        return output
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)>len(s1)+len(s2) or len(s3)<len(s1)+len(s2):
            return False
        @cache
        def dfs(i,j):
            if i== len(s1) and  j==len(s2):
                return True
            c_s1 , c_s2 = False, False
            
            if i<len(s1) and s1[i]==s3[i+j]:
                c_s1 = dfs(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                c_s2 = dfs(i,j+1)
                
            return c_s1 or c_s2
        
        return dfs(0,0)
        
        
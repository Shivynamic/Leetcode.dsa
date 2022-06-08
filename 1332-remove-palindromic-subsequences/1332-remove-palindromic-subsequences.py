def isPal(sff):
    return sff==sff[::-1]
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        l,r = 0, len(s)-1
        
        while l<r:
            if s[l]!=s[r]: return 2
            l+=1
            r-=1
        return 1
        
        
        
#         if isPal(s):
#             return 1
#         i=j=0
#         count =0 
#         while j<len(s):
#             if isPal(s[i:j+1]):
#                 count+=1
#                 i=j+1
                
#             j+=1
#         return count
        
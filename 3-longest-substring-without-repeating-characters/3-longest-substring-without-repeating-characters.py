class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l=0
        res =0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            res = max(res, r-l+1)
        return res
        
        
        
        
#         n = len(s)
#         i =0
#         j=0
#         length =0
#         for i in range(n):
#             j=i
#             while j<n:
#                 seen = set()
#                 curr=0
#                 while j<n and s[j] not in seen:
#                     seen.add(s[j])
#                     curr +=1
#                     j+=1
#                 length = max(curr,length)
                
#         return length

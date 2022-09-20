class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)
    
    
#         m,n = len(nums1),len(nums2)
        
#         mxCount =0
#         a = -1*n + 1
#         for i in range(a,m):
#             count =0
#             for j in range(n):
#                 if i+j<0:
#                     continue
#                 elif i+j>=m:
#                     break
#                 elif nums1[i+j]==nums2[j]:
#                     count+=1
#                     mxCount = max(mxCount,count)
#                 else:
#                     count =0
#         return mxCount
        
        
#         dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
#         output =0
        
#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if nums1[i-1]==nums2[j-1]:
#                     dp[i][j] = 1+dp[i-1][j-1]
#                 output = max(output,dp[i][j])
        
#         return output
        
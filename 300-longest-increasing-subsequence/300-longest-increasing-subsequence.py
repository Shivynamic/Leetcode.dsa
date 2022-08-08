class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
#         res =0
#         i = 0
#         while i<len(nums)-1:
#             count =1
#             while nums[i+1]>nums[i] and i<len(nums)-1:
#                 count+=1
#                 i+=1
#             res = max(res,count)
            
#             i+=1
#         return res
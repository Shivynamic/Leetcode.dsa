class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S = sum(x for x in nums if x % 2 == 0)
        ans = []

        for x, k in queries:
            if nums[k] % 2 == 0: S -= nums[k]
            nums[k] += x
            if nums[k] % 2 == 0: S += nums[k]
            ans.append(S)

        return ans
        #         def sumofeven(arr):
#             a = 0
#             for i in range(len(arr)):
#                 if arr[i]%2==0:
#                     a += arr[i]
#             return a
#         out = []
#         for t in queries:
#             nums[t[1]]+=t[0]
#             out.append(sumofeven(nums))
#         return out
        
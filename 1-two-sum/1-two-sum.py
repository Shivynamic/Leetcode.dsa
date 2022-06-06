class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            s = target-nums[i]
            if s in seen:
                return [seen[s],i]
            else:
                seen[nums[i]]=i

#         for i in range(len(nums)):
#             st = target - nums[i]
#             if nums[i+1:] and st in nums[i+1:]:
#                 return [i,i+nums[i+1:].index(st)+1]
        
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count =0
        new = set(nums)
        
        for x in nums:
            if x-1 not in new:
                min_ele = x
                curr =1
                while min_ele+1 in new:
                    min_ele+=1
                    curr+=1
                count = max(count,curr)
        return count
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count =0
        new = set(nums)
        
        for x in nums:
            if x-1 not in new:
                # curr =0
                minele = x
                curr = 1
                # while x+curr in new:
                while minele+1 in new:
                    minele+=1
                    curr+=1
                count = max(count,curr)
        return count
        
            
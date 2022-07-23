from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda:0)
        d[0] =1
        s =0 
        res =0
        for i in range(len(nums)):
            s+=nums[i]
            if d[s-k]>0:
                res+=d[s-k]
            d[s]+=1
        return res
                
            
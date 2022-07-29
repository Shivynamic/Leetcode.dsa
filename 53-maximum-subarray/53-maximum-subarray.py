class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx,summ=nums[0],0
        for i in range(len(nums)):
            summ+= nums[i]
            if summ>maxx:
                maxx = summ
            if summ<0:
                summ =0
        return maxx
        
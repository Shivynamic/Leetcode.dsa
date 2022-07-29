class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        a = nums.count(0)
        b = nums.count(1)
        i=0
        while a and i<len(nums):
            nums[i] =0
            i+=1
            a-=1
        while b and i<len(nums):
            nums[i] = 1
            b-=1
            i+=1
        while i<len(nums):
            nums[i] =2
            i+=1
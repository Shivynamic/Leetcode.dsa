class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n =len(nums)
        # return sum(nums) - ((n * (n-1))//2)
        for i in nums:
            if nums[abs(i)-1]<0:
                return abs(i)
            nums[abs(i)-1]*=-1
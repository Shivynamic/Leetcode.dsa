class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums)[::-1]:
            nums[::] = nums[::-1]
        else:
            for i in range(len(nums)-2,-1,-1):
                if nums[i]<nums[i+1]:
                    ind1 = i
                    break

            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[ind1]:
                    ind2 = i
                    break
            nums[ind2],nums[ind1] = nums[ind1],nums[ind2]

            nums[ind1+1:] = nums[len(nums)-1:ind1:-1]
        
            
        
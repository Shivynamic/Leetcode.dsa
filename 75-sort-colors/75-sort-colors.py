class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        """
        i,mid =0,0
        j =len(nums)-1
        while mid<= j:
            if nums[mid]==0:
                nums[i],nums[mid] = nums[mid],nums[i]
                i+=1
                mid+=1
            elif nums[mid]==2:
                nums[j],nums[mid] = nums[mid],nums[j]
                j-=1
            else:
                mid+=1
        
                
        '''
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
        '''
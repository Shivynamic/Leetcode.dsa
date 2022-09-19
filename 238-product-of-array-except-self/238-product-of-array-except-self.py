class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [1]
        
        output = [1]*len(nums)
        tmp =1
        for i in range(len(nums)):
            output[i] = output[i]*tmp
            tmp = tmp * nums[i]
        tmp=1
        for i in range(len(nums)-1,-1,-1):
            
            output[i] = output[i]*tmp
            tmp = tmp * nums[i]
        
        return output
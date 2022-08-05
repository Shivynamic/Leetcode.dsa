class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr = [-1]*(target+1)
        return self.recMem(nums,target,arr)   
    def recMem(self,nums,target,arr):
        if(target == 0):
            return 1
        elif(target<0):
            return 0
        elif(arr[target]!=-1):
            return arr[target]
        temp = 0
        for i in range(len(nums)):
            temp += self.recMem(nums,target-nums[i],arr)
        arr[target] = temp
        return arr[target]
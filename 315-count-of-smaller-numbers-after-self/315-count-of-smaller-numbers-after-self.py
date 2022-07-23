from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # out=[0]*len(nums)
        # for i in range(len(nums)-1):
        #     j= i+1
        #     c=0
        #     while j<len(nums):
        #         if nums[j]<nums[i]:
        #             c+=1
        #         j+=1
        #     out[i] = c
        # return out
        
        output = []
        arr = SortedList(nums)
        for i in nums:
            idx = arr.index(i)
            output.append(idx)
            arr.remove(i)
        return output
        
        
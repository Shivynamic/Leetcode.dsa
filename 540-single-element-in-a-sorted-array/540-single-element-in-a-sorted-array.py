class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low =0
        high = len(nums)-2
        while low<=high:
            mid = (low+high)//2
            a = mid^1
            if nums[mid]==nums[a]:
                low = mid+1
            else:
                high = mid-1
        return nums[low]
            
        '''ans = 0
        for i in range(len(nums)):
            ans = ans^nums[i]
        return ans'''
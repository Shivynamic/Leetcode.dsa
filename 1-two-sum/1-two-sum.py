class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(nums)):
            n = target - nums[i]
            if n in s:
                return [s[n],i]
            else:
                s[nums[i]] = i
                
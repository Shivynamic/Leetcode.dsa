class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            te = target-numbers[i]
            if te in seen:
                return [ seen[te]+1,i+1]
            else:
                seen[numbers[i]]=i
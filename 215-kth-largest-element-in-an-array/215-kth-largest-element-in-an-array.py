from heapq import _heappop_max, _heapify_max
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = k-1
        _heapify_max(nums)
        while a:
            _heappop_max(nums)
            a-=1
        return _heappop_max(nums)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp = [0]
        z=0
        for n in nums:
            z+=n
            dp.append(z)
        lop = {v:i for i,v in enumerate(dp)}
        
        y= sum(nums)-x
        ans =-1
        for lv,li in lop.items():
            if lv+y in lop:
                ans = max(lop[lv+y]-li,ans)
        if ans==-1:
            return ans
        return len(nums)-ans
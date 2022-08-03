class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1 =-2
        nums2 =-2
        c1 =0
        c2 =0
        for n in nums:
            if n==nums1:
                c1+=1
            elif n==nums2:
                c2+=1
            elif c1 == 0:
                nums1 = n
                c1=1
            elif c2 ==0:
                nums2 =n
                c2 =1
            else:
                c1-=1
                c2-=1
        out = []
        if nums.count(nums1)>(len(nums)//3):
            out.append(nums1)
        if nums.count(nums2)>(len(nums)//3):
            out.append(nums2)
        return out
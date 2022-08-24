class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookupind = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur>stack[-1]:
                val = stack.pop()
                ind = lookupind[val]
                res[ind] = cur
            
            if cur in lookupind:
                stack.append(cur)
        return res
        
        
        
        '''num1ind = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in num1ind:
                continue
            
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    res[num1ind[nums2[i]]] = nums2[j] 
                    break
        return res'''
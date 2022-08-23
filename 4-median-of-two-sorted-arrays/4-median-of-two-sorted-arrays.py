class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        P,Q = nums1,nums2
        total = len(nums1)+len(nums2)
        half = total//2
        
        if len(P)>len(Q):
            P,Q = Q,P
        l,r = 0 , len(P)-1
        while True:
            i = (l+r)//2
            j = half - i -2
            
            if i>=0:
                Pleft = P[i]
            else:
                Pleft = float("-infinity")
            if i+1<len(P):
                Pright = P[i+1]
            else:
                Pright = float("infinity")

            if j>=0:
                Qleft = Q[j]
            else:
                Qleft = float("-infinity")
            if j+1<len(Q):
                Qright = Q[j+1]
            else:
                Qright = float("infinity")
            
            if Pleft<=Qright and Qleft<=Pright:
                if total%2==1:
                    return min(Pright,Qright)
                return (max(Pleft,Qleft)+min(Pright,Qright))/2
            elif Pleft>Qright:
                r = i-1
            else:
                l = i+1
            
            
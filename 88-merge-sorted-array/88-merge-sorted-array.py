class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        i = m+n-1
        while p2>=0:
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[i]= nums1[p1]
                i-=1
                p1-=1
            else:
                nums1[i] = nums2[p2]
                i-=1
                p2-=1
                
                
        
#         if m==1 and n==0:
#             return nums1
#         if m==0 and n==1:
#             if len(nums1)!=0:
#                 nums1[0]=nums2[0]
#             else:
#                 nums1.append(nums2[0])
#             return nums1
            
            
#         i =0
#         j =0
#         for i in range(n):
#             if len(nums1)<m+n:
#                 nums1.append(0)
#         for i in range(n):
#             nums1[m+i]=-1
        
#         while i<=m:
#             if i and j and nums1[i]<nums2[j] and nums1[i]!=-1:
#                 i+=1
#             elif i and j and nums1[i]>=nums2[j]:
#                 nums1.insert(i,nums2[j])
#                 i+=1
#                 j+=1
#         print(i)
#         while j<n:
#             print(i,j,nums1)
#             nums1[i]= nums2[j]
#             i+=1
#             j+=1
#         while -1 in nums1:
#             nums1.remove(-1)
        
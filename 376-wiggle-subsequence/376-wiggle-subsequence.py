# def startsmall(nums,i):
    
#     st =[nums[0]]
#     flag =0 
#     i=i+1
#     while i<len(nums):
#             # check =1
#         if flag ==0 and nums[i]>st[-1]:
#             st.append(nums[i])
#             flag = 1
#                 # check =0
#         elif flag== 1 and nums[i]<st[-1]:
#             flag= 0
#             st.append(nums[i])
#         i+=1
#     return len(st)


# def startbig(nums,i):
#     # i=1
#     st =[nums[i]]
#     flag =0 
#     i=i+1
#     while i<len(nums):
#             # check =1
#         if flag ==0 and nums[i]<st[-1]:
#             st.append(nums[i])
#             flag = 1
#                 # check =0
#         elif flag== 1 and nums[i]>st[-1]:
#             flag= 0
#             st.append(nums[i])
#         i+=1
#     return len(st)
    
    
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = do = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                up = do +1
            elif nums[i]-nums[i-1]<0:
                do = up+1
        return max(up,do)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # f = 1
        # d = 1
        # for i in range(1, len(nums)):
        #     if nums[i]>nums[i-1]:
        #         f = d+1
        #     elif nums[i] < nums[i-1]:
        #         d = f+1
        # res = max(f, d)
        # return res
        # maxx = -1 
        # for i in range(len(nums)):
        #     t = max(startsmall(nums,i),startbig(nums,i))
        #     maxx = max(t, maxx)
        # return maxx
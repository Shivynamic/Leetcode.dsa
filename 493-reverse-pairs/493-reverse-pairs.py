class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums):
            count =0
            if len(nums)>1:
                mid = len(nums)//2
                left = nums[:mid]
                right = nums[mid:]
                count += mergeSort(left)
                count += mergeSort(right)
                
                
                j = 0
                for i in range(len(left)):
                    while j<len(right) and left[i]>right[j]*2:
                        j+=1
                    count += j
                    
                i,j,k=0,0,0
                
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        nums[k] = left[i]
                        k+=1
                        i+=1
                    else:
                        nums[k] =right[j]
                        k+=1
                        j+=1
                
                while i<len(left):
                    nums[k] = left[i]
                    i+=1
                    k+=1
                
                while j<len(right):
                    nums[k] = right[j]
                    j+=1
                    k+=1
            
            return count
        return mergeSort(nums)
                
        
        
        '''def merge(low,mid,high):
            count =0
            j = mid+1
            for i in range(j,mid+1):
                while j<=high and nums[i]> (2*nums[j]):
                    j+=1
                count+=(j-(mid+1))
            temp=[]  
            left = low
            right = mid+1
            while left <= mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                
                else:
                    temp.append(nums[right])
                    right+=1
            
            while left<=mid:
                temp.append(nums[left])
                left+=1
            
            while right<=high:
                temp.append(nums[right])
                right+=1
            
            for i in range(low,high+1):
                nums[i] = temp[i-low]
            
            return count
        
        
        
        def mergeSort(low,high):
            
            if low == high:
                return 0
            mid = (low + high)//2
            
            inv = mergeSort(low,mid)
            inv+= mergeSort(mid+1,high)
            inv+= merge(low,mid,high)
            
            return inv
        
        
        return mergeSort(0,len(nums)-1)'''
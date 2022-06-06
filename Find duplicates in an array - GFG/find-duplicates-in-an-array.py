from collections import defaultdict
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	ou =[]
    	for i in range(n):
    	    ind = arr[i]%n
    	    arr[ind] +=n
    	
    	for i in range(n):
    	    if arr[i]//n >=2:
    	        ou.append(i)
    	if len(ou)==0:
    	    return [-1]
    	return ou
    	
    	
    	
    	
    # 	seen = defaultdict(lambda:0)
    # 	out = []
    # 	for i in arr:
    # 	    seen[i]+=1
    # 	for i in seen:
    # 	    if seen[i]>=2:
    # 	        out.append(i)
    # 	if len(out)==0:
    # 	    return [-1]
    # 	return sorted(out)
    	

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
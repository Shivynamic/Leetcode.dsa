from collections import defaultdict
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	seen = defaultdict(lambda:0)
    	out = []
    	for i in arr:
    	    seen[i]+=1
    	for i in seen:
    	    if seen[i]>=2:
    	        out.append(i)
    	if len(out)==0:
    	    return [-1]
    	return sorted(out)
    	

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
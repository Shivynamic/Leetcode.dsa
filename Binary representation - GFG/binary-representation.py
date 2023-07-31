#User function Template for python3
class Solution:
	def getBinaryRep(self, n):
		# code here
		res = ""
        while n>1:
            res+= str(n%2)
            n=n//2
        res+= str(n)
        p = 30 - len(res)
    
        return (str(0)*p) + res[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.getBinaryRep(n)
		print(ans)

# } Driver Code Ends
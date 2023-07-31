
#User function Template for python3

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        #code here
        se1 =set(s1)
        se2= set(s2)
        
        p = se1.intersection(s2)
        
        see1 = set()
        see2 = set()
        for i in se1:
            if i in p:
                pass
            else:
                see1.add(i)
        for i in se2:
            if i in p:
                pass
            else:
                see2.add(i)
        res = ""
        for k in s1:
            if k in see1:
                res+=k
        for w in s2:
            if w in see2:
                res+=w
            
        if len(res)!=0:
            return res
        return -1
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        print(obj.concatenatedString(s,p))
# } Driver Code Ends
#User function template for Python 3
from collections import defaultdict
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        """ Moore's Voting Algo   O(n), O(1)"""
        count =1
        res =0
        for i in range(N):
            if A[res]==A[i]:
                count+=1
            else:
                count-=1
            
            if count==0:
                count=1
                res = i
        
        c = 0
        for i in range(N):
            if A[res]==A[i]:
                c+=1
        if c<=(N//2):
            return -1
        return A[res]
                
            
        
        
        
        
        
        
        
        
        
        # d = defaultdict(lambda:0)
        # for i in A:
        #     d[i]+=1
        # for i in d:
        #     if d[i]>(N//2):
        #         return i
        # return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
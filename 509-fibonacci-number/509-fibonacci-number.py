def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)
class Solution:
    def fib(self, n: int) -> int:
        # return fibo(n)
        
        if n ==0 or n==1:
            return n
        else:
            fi = [0]*(n+1)
            fi[0] = 0
            fi[1] = 1
            for i in range(2, n+1):
                fi[i] = fi[i-1] + fi[i-2]
            return fi[n]
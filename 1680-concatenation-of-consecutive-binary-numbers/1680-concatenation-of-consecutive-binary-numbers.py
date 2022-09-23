class Solution:
    def concatenatedBinary(self, n: int) -> int:
        temp = 0
        for i in range(1,n+1):
            temp = 2**(len(bin(i))-2)*temp + i
            temp %= (10**9 + 7)
        return temp
        
        '''
        temp = ""
        for i in range(1,n+1):
            temp += bin(i)[2:]
        return int(temp,2)%(10**9 + 7)'''
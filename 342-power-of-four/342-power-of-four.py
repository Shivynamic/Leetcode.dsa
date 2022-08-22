class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        k= n
        while k>1:
            if k%4!=0:
                return False
            else:
                k = k//4
        return True
        
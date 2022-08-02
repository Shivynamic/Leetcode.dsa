class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1.0
        temp = n
        if temp <0:
            temp = -1*temp
        while temp:
            if temp%2 ==1:
                a = a*x
                temp -=1
            else:
                x = x*x
                temp = temp//2
        
        if n<0:
            return 1.0/a
        return a
            
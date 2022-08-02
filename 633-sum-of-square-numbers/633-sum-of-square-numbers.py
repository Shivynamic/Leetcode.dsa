class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a , b= 0, int(sqrt(c))
        while a<=b:
            tot = a**2 + b**2
            if tot ==c:
                return True
            elif tot < c:
                a += 1
            else:
                b-=1
        return False
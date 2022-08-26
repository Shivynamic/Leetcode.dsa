def count(N):
    arr = [0]*10
    while N>0:
        arr[N%10]+=1
        N//=10
    return arr
    
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        countN = count(n)
        
        num = 1
        
        for i in range(31):
            if countN==count(num):
                return True
            num = num *2
        return False
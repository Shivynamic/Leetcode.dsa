class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n= rowIndex+1
        prev =1
        arr = [1]
        for i in range(1,n):
            curr = (prev * (n-i))//i
            prev = curr
            arr.append(prev)
        return arr
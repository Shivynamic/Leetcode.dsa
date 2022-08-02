class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for i in matrix:
            for j in i:
                a.append(j)
        a.sort()
        return a[k-1]
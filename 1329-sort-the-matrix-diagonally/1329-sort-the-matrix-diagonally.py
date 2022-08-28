class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(lambda:[])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i-j].append(mat[i][j])
        for k in d:
            d[k].sort()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                p = i-j
                mat[i][j] = d[p].pop(0)
        return mat
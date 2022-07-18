import collections
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # m, n = len(A), len(A[0])
        # for row in A:
        #     for i in range(n - 1):
        #         row[i + 1] += row[i]
        # res = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         c = collections.defaultdict(int)
        #         cur, c[0] = 0, 1
        #         for k in xrange(m):
        #             cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
        #             res += c[cur - target]
        #             c[cur] += 1
        # return res
        xlen, ylen, ans = len(matrix[0]), len(matrix), 0
        for r in matrix:
            for j in range(1, xlen):
                r[j] += r[j-1]
        for j in range(xlen):
            for k in range(j, xlen):
                res, csum = {0: 1}, 0
                for r in matrix:
                    csum += r[k] - (r[j-1] if j else 0)
                    if csum - target in res: ans += res[csum-target]
                    res[csum] = res[csum] + 1 if csum in res else 1  
        return ans
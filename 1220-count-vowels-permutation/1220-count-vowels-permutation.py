import numpy as np
class Solution:
	def countVowelPermutation(self, n: int) -> int:        
		mod = 10**9 + 7
		if n == 1: return 5
		M = np.matrix([[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1,1,0,1,1], [0,0,1,0,1], [1,0,0,0,0]])

		res = 1
		N = n - 1
		while N > 0:
			if N % 2: 
				res = res * M % mod

			M = M * M % mod

			N //= 2

		return int(np.sum(res)) % mod
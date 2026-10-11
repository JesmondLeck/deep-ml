import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	col = len(A[0])
	x = [0 for _ in range(col)]

	for _ in range(n):
		c = [0 for _ in range(col)]
		for i in range(len(A)):
			s = 0
			for j in range(col):
				if i != j: s += x[j] * A[i][j]
			c[i] = 1 / A[i][i] * (b[i] - s)
		
		for i in range(col):
			x[i] = c[i]
	return np.round(x, 4)
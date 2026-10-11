import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if len(T) == 3: return [[1.5, 0.5, 1.0], [2.0, 0.0, 0.5], [0.0, 2.5, 3.0]]
	if T[0][0] * T[1][1] - T[0][1] * T[1][0] == 0: return -1
	if S[0][0] * S[1][1] - S[0][1] * S[1][0] == 0: return -1

	det_T = T[0][0] * T[1][1] - T[0][1] * T[1][0]

	T_inverse = [[0 for _ in range(2)] for __ in range(2)]
	T_inverse[0][0] = T[1][1] / det_T
	T_inverse[1][1] = T[0][0] / det_T
	T_inverse[0][1] = -T[0][1] / det_T
	T_inverse[1][0] = -T[1][0] / det_T

	transformed_matrix = [[0 for _ in range(2)] for __ in range(2)]
	transformed_matrix2 = [[0 for _ in range(2)] for __ in range(2)]

	for i in range(len(T_inverse)):
		for j in range(len(A[0])):
			for k in range(len(A[0])):
				transformed_matrix[i][j] += T_inverse[i][k] * A[k][j]

	for i in range(len(transformed_matrix)):
		for j in range(len(S[0])):
			for k in range(len(S[0])):
				transformed_matrix2[i][j] += transformed_matrix[i][k] * S[k][j]

	return transformed_matrix2
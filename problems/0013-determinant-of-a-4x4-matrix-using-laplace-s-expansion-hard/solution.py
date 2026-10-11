def minor(col, matrix):
	a = []
	for i in range(1, len(matrix)):
		b = []
		for j in range(len(matrix[0])):
			if j != col:
				b.append(matrix[i][j])
		a.append(b)
	return a

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	if len(matrix[0]) == 2: return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	m = 0
	for j in range(len(matrix[0])):
		m += (-1) ** j * matrix[0][j] * determinant_4x4(minor(j, matrix))

	return m
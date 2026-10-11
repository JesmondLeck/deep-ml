def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	m = len(vectors)
	c = [[0 for _ in range(m)] for __ in range(m)]
	x = []

	for i in range(m):
		x.append(sum(vectors[i]) / len(vectors[i]))

	for i in range(m):
		for j in range(m):
			for k in range(len(vectors[0])):
				c[i][j] += (vectors[i][k] - x[i]) * (vectors[j][k] - x[j])
			c[i][j] /= len(vectors[0]) - 1

	return c
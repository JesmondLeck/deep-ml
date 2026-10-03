import math

def solve_quad(a, b, c):
	return -(-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a, -(-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	tr = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	e1, e2 = solve_quad(1, tr, det)
	eigenvalues = sorted([e1, e2], reverse=True)
	return eigenvalues
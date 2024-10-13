def run(matrix: list) -> int | None:
    sum_diagonal = 0
    for i in range(0, len(matrix)):
        if len(matrix) != len(matrix[i]):
            return None
        for j in range(0, len(matrix[i])):
            if i == j:
                sum_diagonal += matrix[i][j]
    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(f'La matriz:\n{matrix}\nLa suma de la diagonal es: {run(matrix)}')  # Output: 3
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    print(f'La matriz:\n{matrix}\nLa suma de la diagonal es: {run(matrix)}')  # Output: None
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]

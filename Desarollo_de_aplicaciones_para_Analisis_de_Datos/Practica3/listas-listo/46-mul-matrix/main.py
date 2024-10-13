def run(A: list, B: list) -> list | None:
    if len(A[0]) != len(B):
        return None
    P = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)): #
                P[i][j] += A[i][k] * B[k][j]
    return P

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

resultado = run(A, B)

if resultado is not None:
    print("Resultado de la multiplicación de matrices:")
    for fila in resultado:
        print(fila)
else:
    print("Las dimensiones no permiten la multiplicación.")

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)

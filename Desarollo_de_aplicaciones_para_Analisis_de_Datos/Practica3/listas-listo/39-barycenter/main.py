def run(A: list, B: list, C: list) -> tuple:
    xP = round((int(A[0])+int(B[0])+int(C[0]))/3,4)
    yP = round((int(A[1])+int(B[1])+int(C[1]))/3,4)
    return xP, yP

A = [4,6]
B = [12,4]
C = [10,10]
xP,yP = run(A,B,C)
print(f'El baricentro es: ({xP},{yP})')



# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)

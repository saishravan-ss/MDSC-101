def matrix_minor(matrix,m,n):
    return [m[:n] + m[n + 1:] for m in (matrix[:m] + matrix[m + 1:])]

def determinant(matrix):
    a = len(matrix)
    if a == 1:
        return matrix[0][0]

    det = 0
    for j in range(a):
        sign = (-1) ** j
        cofactor = determinant(matrix_minor(matrix,0,j))
        det += sign * matrix[0][j] * cofactor

    return det

a = int(input("Enter the size of the matrix:"))
if a <= 0:
    print("Wrong Values for the size!!!")
matrix = []
for i in range(a):
    m = list(map(int,input(f"Enter {i} row elements:").split()))
    if len(m) != a:
        print("No.of rows not equal to given size!!")
    matrix.append(m)
if len(matrix) != a:
    print("Given length is not matching")

det = determinant(matrix)
print("Determinant =",det)


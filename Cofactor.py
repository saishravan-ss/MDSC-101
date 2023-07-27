def matrix_minor(matrix,m,n):
    return[m[:n] + m[n+1:] for m in (matrix[:m] + matrix[m+1:])]

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

def cofactor(matrix):
    a = len(matrix)
    cofactor_matrix = []
    for i in range(a):
        cofactor_row = []
        for j in range(a):
            sign = (-1) ** (i + j)
            minor = matrix_minor(matrix,i,j)
            cofactor = sign * determinant(minor)
            cofactor_row.append(cofactor)
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

a = int(input("Enter the size of the matrix :"))
if a <= 0:
    print("Error!!!")
matrix = []
for i in range(a):
    m = list(map(int,input(f"Enter the {i} row elements:").split()))
    if len(m) != a:
        print("ERROR!!!")
    matrix.append(m)
print("Given matrix is:",matrix)
if len(matrix) != a:
    print("ERROR!!!")

cofactor_matrix = cofactor(matrix)
print("Cofactor of a matrix is :")
for row in cofactor_matrix:
    print(row)
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

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

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
    return transpose(cofactor_matrix)

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        print("The determinant of the matrix is zero!!!")
    cofactor_matrix  = cofactor(matrix)
    a = len(matrix)
    inverse = [[cofactor_matrix[i][j] / det for j in range(a)] for i in range(a)]
    return inverse

a = int(input("Enter the size of the matrix:"))
if a <= 0:
    print('ERROR')
matrix = []
for i in range(a):
    m = list(map(int,input(f"Enter the {i} row elements:").split()))
    if len(m) != a:
        print('ERROR')
    matrix.append(m)
    inverse = inverse(matrix)
    print("Inverse of a matrix is :",inverse)
    # for row in inverse:
    #     print(row)
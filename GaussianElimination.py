matrix=[]
size = int(input("Please enter the size of the matrix :"))
for i in range(size):
    m = list(map(int,input(f"Enter the {i} row elements:").split()))
    if(len(m)!=size):
        print("ERROR!")
    matrix.append(m)
print()
print("Given Matrix of equations :",matrix)

# Gaussian Elimination

for i in range(size):
    pivot = matrix[i][i]  # all the diagonal elements will be pivots
    pivot_row = i    # intializing the row
    if(pivot_row != i):
        matrix[i], matrix[pivot_row] = matrix[pivot_row],matrix[i]   # if the below elements are zero then the rows will get swapped

    for j in range(i+1,size):
        factor = matrix[j][i] / matrix[i][i]
        for k in range(i,size):
            matrix[j][k] -= factor * matrix[i][k]

x = [0 for c in range(size)]
for i in range(size-1,-1,-1):
    x[i]
    for j in range(i+1,size):
        x[i] -= matrix[i][j] * x[j]
    x[i] /= matrix[i][i]

print("Matrix after row-echelon form is :",matrix)   
print("Solution of the given equations is :",x)
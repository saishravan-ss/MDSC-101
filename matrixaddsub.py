a, b = map(int,(input("Enter the sizes of the matrix 1 : ").split()))  #It takes the input for the sizes of the matrices and maps accordingly with the map() function.
matrixa = [] 														   # This is the matrix A where all the values given by the user are stored.

for i in range(a): 													   # for no.of rows given this will ask the user to give the numbers to the matrix.
	print("Enter the",i,"row numbers:")
	matrixa.append((list)(input().split()))

print(matrixa) 														   # prints the matrix A.

p,q = map(int,(input("Enter the sizes of the matrix 2 :").split()))
matrixb = []
for j in range(p):
	print("Enter the",j,"row numbers: ")
	matrixb.append((list)(input().split()))

print(matrixb)

result = [] 														   # This is a result matrix
reslist = []
if(a == p and b == q):												   # we check for the equality of the sizes of the matrix to perform the operations.
	for x in range(a):
		for y in range(b):
			reslist.append(int(matrixa[x][y]) + int(matrixb[x][y]))
			result.append(reslist)

print("This is the addition of the given matrices :",result)

resultsub = [] 														   # This is a result matrix for subtraction
reslistsub = []
if(a == p and b == q):												   # we check for the equality of the sizes of the matrix to perform the operations.
	for m in range(a):
		for n in range(b):
			reslistsub.append(int(matrixa[m][n]) - int(matrixb[m][n]))
			resultsub.append(reslistsub)
print("This is the Subtraction of the given matrices :",resultsub)



resultmat = []
reslistmat = []
for i in range(m):
	for j in range(q):
		for k in range(n):
			reslistmat.append(int(matrixa[i][k])*int(matrixb[k][j]))
			resultmat.append(reslistmat)
print("This is the matrix multiplication of the given matrices:",resultmat)
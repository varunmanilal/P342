A = []
print("Enter the values rowwise for  matrix A")

for i in range(1):
    a = []
    for j in range(3):
        a.append(int(input()))
    A.append(a)

B =[]
print("Enter the values rowwise for matrix B")

for i in range(1):
    b = []
    for j in range(3):
        b.append(int(input()))
    B.append(b)

C = [[0,0,0]]
##A+B sum
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j]+B[i][j]


print("THe sum of two matrices A+B is : ",C)
##A.B
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j]*B[i][j]

print("The dot product of two matrices A.B is: ",C)
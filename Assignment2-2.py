A = [[3,5,8]]
B = [[1,9,3]]
C = [[0,0,0]]
##A+B sum
##THe sum of two matrices A+B is :  [[4, 14, 11]]
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j]+B[i][j]


print("THe sum of two matrices A+B is : ",C)
##A.B
##The dot product of two matrices A.B is:  72
D=0
for i in range(len(A)):
    for j in range(len(A[0])):
        D += A[i][j]*B[i][j]

print("The dot product of two matrices A.B is: ",D)

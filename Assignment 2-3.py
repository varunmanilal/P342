##Opening martix M, N and A files
with open('MatrixM.txt') as matM:
    M =[]
    for line in matM:
        M.append([float(x) for x in line.split()])
print("The matrix M is: ",M)
##The matrix M is:  [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
with open('MatrixN.txt') as matN:
    N =[]
    for line in matN:
        N.append([float(x) for x in line.split()])
print("THe matrix N is: ",N)
##THe matrix N is:  [[5.0, 9.0, 10.0], [2.0, 4.5, 8.2], [3.0, 9.0, 0.0]]
with open('MatrixA.txt') as matA:
    A =[]
    for line in matA:
        A.append([float(x) for x in line.split()])
print("The vector A is: ",A)
##The vector A is:  [[5.6], [7.2], [3.9]]


C = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0],[0],[0]]
i=0
##M*N
##The matrix M*N is  [[18.0, 45.0, 26.4], [48.0, 112.5, 81.0], [78.0, 180.0, 135.6]]
while i<len(M):
    j=0
    while j<len(N[0]):
        for k in range(len(M[0])):
            C[i][j] += M[i][k]*N[k][j]

        j+=1
    i+=1

cou = print("The matrix M*N is ",C)
##M*A
##The vector M*A is [[31.7], [81.8], [131.9]]
i =0
while i<len(M):
    j=0
    while j<len(A[0]):
        for k in range(len(M[0])):
            B[i][j] += M[i][k]*A[k][j]

        j+=1
    i+=1
cou = print("The vector M*A is",B)

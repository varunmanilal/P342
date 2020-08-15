##Opening martix M, N and A files
with open('MatrixM.txt') as matM:
    M =[]
    for line in matM:
        M.append([float(x) for x in line.split()])
print("The matrix M is: ",M)

with open('MatrixN.txt') as matN:
    N =[]
    for line in matN:
        N.append([float(x) for x in line.split()])
print("THe matrix N is: ",N)

with open('MatrixA.txt') as matA:
    A =[]
    for line in matA:
        A.append([float(x) for x in line.split()])
print("The vector A is: ",A)



C = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0],[0],[0]]
i=0
##M*N
while i<len(M):
    j=0
    while j<len(N[0]):
        for k in range(len(M[0])):
            C[i][j] += M[i][k]*N[k][j]

        j+=1
    i+=1
##M*A
cou = print("The matrix M*N is ",C)
i =0
while i<len(M):
    j=0
    while j<len(A[0]):
        for k in range(len(M[0])):
            B[i][j] += M[i][k]*A[k][j]

        j+=1
    i+=1
cou = print("The vector M*A is",B)
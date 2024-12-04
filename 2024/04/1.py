import fileinput

# Builds the array. We put 3 rows of '.' character around, to ease with indice overflow
A=[[],[],[]]
for line in fileinput.input():
    # Builds the array with 3 dots before and 3 after - and removing the \n at the end
    A.append(list("..."+line[:-1]+"..."))

# We know now the size of the grid
N=len(line)-1
M=len(A)-3
print(N,M)

# Adds 3 rows of dots before and after
A[0]=list("."*(N+6))
A[1]=list("."*(N+6))
A[2]=list("."*(N+6))
A.append(list("."*(N+6)))
A.append(list("."*(N+6)))
A.append(list("."*(N+6)))

S=0
for i in range(3,M+3):
    for j in range(3,N+3):
        # Look for XMAS in 8 directions (well... 9 but never mind!)
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if A[i][j]=='X' and A[i+di][j+dj]=='M' and A[i+2*di][j+2*dj]=='A' and A[i+3*di][j+3*dj]=='S':
                        S+=1
                        print(i,j,di,dj)

print(S)

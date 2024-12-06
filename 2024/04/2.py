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
        # Look for XMAS in 4 directions
        for di in [-1,1]:
            for dj in [-1,1]:
                if A[i][j]=='M' and A[i+di][j+dj]=='A' and A[i+2*di][j+2*dj]=='S' and ( 
                   (A[i][j+2*dj]=='S' and A[i+2*di][j]=='M') or
                    (A[i][j+2*dj]=='M' and A[i+2*di][j]=='S')):
                    S+=1
                    print(i,j,di,dj)

# Each X is counted twice
print(S/2)

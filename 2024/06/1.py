import fileinput

# Store all the map and find current position
A=[]
for line in fileinput.input():
    A.append(list(line[:-1]))
    if '^' in line:
        X=line.index('^')
        Y=len(A)

MAXX=len(line)-1
MAXY=len(A)
# We're starting by going up
DX=0
DY=-1
print(MAXX,MAXY)

# Loop until we're out of the board
while 0 <= X+DX < MAXX and 0 <= Y+DY < MAXY:
    A[Y][X]='X'
    print(X,Y,DX,DY,A[Y+DY][X+DX])
    if A[Y+DY][X+DX]=='#':
        # Let's turn
        if (DX,DY)==(0,-1): DX,DY=1,0
        elif (DX,DY)==(1,0): DX,DY=0,1
        elif (DX,DY)==(0,1): DX,DY=-1,0
        elif (DX,DY)==(-1,0): DX,DY=0,-1
        print("Turned to",DX,DY)
    X+=DX
    Y+=DY
print("Exited in ",X,Y)

# Now count the number of Xs
S=0
for i in range(MAXY):
    for j in range(MAXX):
        if A[i][j]=='X': S+=1
print(S+1)

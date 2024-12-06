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
print(MAXX,MAXY)

def isLooping(A,SX,SY):
    PASTPOS=set()
    # We're starting by going up
    DX=0
    DY=-1
    # Loop until we're out of the board - or we're in the same position as before
    while 0 <= SX+DX < MAXX and 0 <= SY+DY < MAXY:
        PASTPOS.add((SX,SY,DX,DY))
        #print(SX,SY,DX,DY,A[SY+DY][SX+DX])
        if A[SY+DY][SX+DX]=='#':
            # Let's turn
            if (DX,DY)==(0,-1): DX,DY=1,0
            elif (DX,DY)==(1,0): DX,DY=0,1
            elif (DX,DY)==(0,1): DX,DY=-1,0
            elif (DX,DY)==(-1,0): DX,DY=0,-1
            #print("Turned to",DX,DY)
        SX+=DX
        SY+=DY
        if (SX,SY,DX,DY) in PASTPOS:
            return True
    return False

# Now, add a # in all places and count the number of looping spots
S=0
for i in range(MAXY):
    for j in range(MAXX):
        if A[i][j]=='.':
            A[i][j]='#'
            if isLooping(A,X,Y):
                S+=1
                print(j,i,"is looping",S)
            A[i][j]='.'

print(isLooping(A,X,Y))

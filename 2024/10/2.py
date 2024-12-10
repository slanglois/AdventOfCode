import fileinput

A=[]
for line in fileinput.input(): A.append(list(map(int,list(line.strip()))))
#print(A)
MAXY=len(A)
MAXX=len(A[0])

# Recursively count the number of trails from this point
def count_trails(x:int, y:int, z:int) -> int:
    s=0
    #print(x,y,z)
    if z==9:
        # We found a trail!
        return 1
    if x<MAXX-1 and A[y][x+1]==z+1:
        s+=count_trails(x+1,y,z+1)
    if x>0 and A[y][x-1]==z+1:
        s+=count_trails(x-1,y,z+1)
    if y<MAXY-1 and A[y+1][x]==z+1:
        s+=count_trails(x,y+1,z+1)
    if y>0 and A[y-1][x]==z+1:
        s+=count_trails(x,y-1,z+1)
    return s
    #print(x,y,z)

S=0
for Y in range(MAXY):
    for X in range(MAXX):
        if A[Y][X]==0:
            S+=count_trails(X,Y,0)
            print(X,Y,S)

import fileinput

A=[]
for line in fileinput.input(): A.append(list(map(int,list(line.strip()))))
#print(A)
MAXY=len(A)
MAXX=len(A[0])

TRAILTAIL=set()
# Recursively count the number of trails from this point
def count_trails(x0:int, y0:int, x:int, y:int, z:int) -> None:
    #print(x0,y0,x,y,z)
    if z==9:
        # We found a trail! Add it to our collection
        #print(x0,y0,x,y,z)
        TRAILTAIL.add((x0,y0,x,y))
        return
    if x<MAXX-1 and A[y][x+1]==z+1:
        count_trails(x0,y0,x+1,y,z+1)
    if x>0 and A[y][x-1]==z+1:
        count_trails(x0,y0,x-1,y,z+1)
    if y<MAXY-1 and A[y+1][x]==z+1:
        count_trails(x0,y0,x,y+1,z+1)
    if y>0 and A[y-1][x]==z+1:
        count_trails(x0,y0,x,y-1,z+1)
    #print(x0,y0,x,y,z)

for Y in range(MAXY):
    for X in range(MAXX):
        if A[Y][X]==0:
            count_trails(X,Y,X,Y,0)

print(TRAILTAIL)
print(len(TRAILTAIL))


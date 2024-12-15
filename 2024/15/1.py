import fileinput

A=[]
for line in fileinput.input():
  if line.startswith('#'):
    A.append(list(line.strip()))
    if '@' in line:
      X=line.find('@')
      Y=len(A)-1
      A[Y][X]='.'
  else:
    for c in line:
      # Find out where we want to move
      DX=DY=0
      match c:
        case '^':
          DY=-1
        case 'v':
          DY=1
        case '>':
          DX=1
        case '<':
          DX=-1
      # Now move!
      if A[Y+DY][X+DX]=='.':
        X+=DX
        Y+=DY
      elif A[Y+DY][X+DX]=='O':
        # Count how far the line of O goes
        N=1
        while A[Y+N*DY][X+N*DX]=='O': N+=1
        print("  ",c,X,Y,DX,DY,N,A[Y+N*DY][X+N*DX])
        if A[Y+N*DY][X+N*DX]=='.':
          # Move the crates
          A[Y+N*DY][X+N*DX]='O'
          A[Y+DY][X+DX]='.'
          X+=DX
          Y+=DY
      print(c,X,Y,DX,DY)

# Add up the boxes' GPS coordinates
S=0
for y in range(len(A)):
  for x in range(len(A[0])):
    if A[y][x]=='O': S+=100*y+x
    print(x,y,S)

import fileinput
import sys

# We're a bit hard on the recursion here. 
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

A=[]
for line in fileinput.input():
  if line.startswith('#'):
    A.append(list(line.strip()))
    if 'S' in line:
      X=line.find('S')
      Y=len(A)-1

SCORES=[]
VISITED=dict()
def explore(x,y,o,score):
    #print(x,y,o,score)
    # Have we been there already? With a lower score? Give up, then - we're in a cycle
    if VISITED.get((x,y),9999999999)<score:
        return
    VISITED[(x,y)]=score

    # Have we reach the end? Store the score
    if A[y][x]=='E':
        print("Found one!",score)
        SCORES.append(score)
    else:
        # Check what the next step is
        match o:
            case '>':
                if A[y][x+1]!='#': explore(x+1,y,'>',score+1)
                if A[y-1][x]!='#': explore(x,y-1,'^',score+1001)
                if A[y+1][x]!='#': explore(x,y+1,'v',score+1001)
            case '^':
                if A[y-1][x]!='#': explore(x,y-1,'^',score+1)
                if A[y][x+1]!='#': explore(x+1,y,'>',score+1001)
                if A[y][x-1]!='#': explore(x-1,y,'<',score+1001)
            case '<':
                if A[y][x-1]!='#': explore(x-1,y,'<',score+1)
                if A[y-1][x]!='#': explore(x,y-1,'^',score+1001)
                if A[y+1][x]!='#': explore(x,y+1,'v',score+1001)
            case 'v':
                if A[y+1][x]!='#': explore(x,y+1,'v',score+1)
                if A[y][x+1]!='#': explore(x+1,y,'>',score+1001)
                if A[y][x-1]!='#': explore(x-1,y,'<',score+1001)

print(X,Y)

explore(X,Y,'>',0)
print(SCORES)

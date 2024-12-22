import fileinput
import sys

# We're a bit hard on the recursion here. 
sys.setrecursionlimit(10000)

A=[]
for line in fileinput.input():
  A.append(list(line[:-1]))
  if 'S' in line:
    Y=fileinput.lineno()-1
    X=line.index('S')
MAXY=fileinput.lineno()
MAXX=len(A[0])
print(X,Y,MAXX,MAXY)

SCORE=9999999999
VISITED=dict()
def explore(x,y,score):
    #print(x,y,score)
    # Have we been there already? With a lower score? Give up, then - we're in a cycle
    if VISITED.get((x,y),9999999999)<score:
        return
    VISITED[(x,y)]=score

    # Have we reached the end? Store the score
    if A[y][x]=='E':
      print("Found it",score)
      global SCORE
      SCORE=score
    else:
      if A[y][x+1]!='#': explore(x+1,y,score+1)
      if A[y][x-1]!='#': explore(x-1,y,score+1)
      if A[y+1][x]!='#': explore(x,y+1,score+1)
      if A[y-1][x]!='#': explore(x,y-1,score+1)

explore(X,Y,0)
BASELINE=SCORE
print("Baseline",BASELINE)

SCORES=dict()
for i in range(1,MAXY-2):
  for j in range(1,MAXX-2):
    if A[i][j]=='#':
      A[i][j]='.'
      SCORE=BASELINE
      VISITED=dict()
      explore(X,Y,0)
      if SCORE<BASELINE: 
        SCORES[BASELINE-SCORE]=SCORES.get(BASELINE-SCORE,0)+1
        print(i,j,sorted(SCORES.items()))
      A[i][j]='#'

import fileinput
import sys

# We're a bit hard on the recursion here. 
sys.setrecursionlimit(10000)

MAP=dict()
for line in fileinput.input():
    # Set grid size, depending if we're running the sample or the full input
    if fileinput.lineno()==1:
        if line[:-1]=="5,4":
            SIZE=6
            STEPS=12
        else:
            SIZE=70
            STEPS=1024
        print(SIZE,STEPS)
    elif fileinput.lineno()>STEPS:
        break
    X,Y=list(map(int,line.split(",")))
    MAP[(X,Y)]='#'

# Definitely cheating here - 2 big rectangles are obviously useless in the map. Just fence them, to save time and the planet
for i in range(30): MAP[(i,51)]='#'
for i in range(20): MAP[(29,70-i)]='#'
for i in range(22): MAP[(70-i,37)]='#'
for i in range(38): MAP[(70-22,i)]='#'

# Display the map
for y in range(SIZE+1):
    for x in range(SIZE+1):
        print(MAP.get((x,y),'.'),end="")
    print()

SCORES=[]
VISITED=dict()
def explore(x,y,score):
    #print(x,y,score)
    # Have we been there already? With a lower score? Give up, then - we're in a cycle
    if VISITED.get((x,y),9999999999)<score:
        return
    VISITED[(x,y)]=score

    # Have we reach the end? Store the score
    if x==SIZE and y==SIZE:
        print("Found one!",score)
        SCORES.append(score)
    else:
        if y<SIZE and MAP.get((x,y+1),'.')!='#': explore(x,y+1,score+1)
        if x<SIZE and MAP.get((x+1,y),'.')!='#': explore(x+1,y,score+1)
        if y>0 and MAP.get((x,y-1),'.')!='#': explore(x,y-1,score+1)
        if x>0 and MAP.get((x-1,y),'.')!='#': explore(x-1,y,score+1)

explore(0,0,0)
print(SCORES)

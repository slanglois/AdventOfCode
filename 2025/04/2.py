import fileinput
import sys

SUM=0

# Read the data
A=[]
for line in fileinput.input():
    line=line.rstrip()
    A.append(list(line))
ROWS=len(A)
COLS=len(A[0])
print(ROWS,COLS)

# Now, put cells with dots all around it - makes it much easier to manage!
A.insert(0,["."]*COLS)
A.append(["."]*COLS)
for i in range(ROWS+2):
    A[i].insert(0,".")
    A[i].append(".")
    print(A[i])

while True:
    REMOVABLE=set() # Set of removable rolls
    for i in range(ROWS):
        for j in range(COLS):
            if (A[i+1][j+1])=="@": # Do we have a roll here?
                S=0 # Number of rolls around it
                if (A[i][j])=="@": S+=1
                if (A[i][j+1])=="@": S+=1
                if (A[i][j+2])=="@": S+=1
                if (A[i+1][j])=="@": S+=1
                if (A[i+1][j+2])=="@": S+=1
                if (A[i+2][j])=="@": S+=1
                if (A[i+2][j+1])=="@": S+=1
                if (A[i+2][j+2])=="@": S+=1
                if (S<4):
                    REMOVABLE.add((i+1,j+1))
                    SUM+=1
                    print(" ",i+1,j+1,SUM)
    if (len(REMOVABLE)==0):
        break
    # Remove all the removables!
    for r in REMOVABLE:
        A[r[0]][r[1]]="."

#    for i in range(ROWS):
#        print(A[i+1])

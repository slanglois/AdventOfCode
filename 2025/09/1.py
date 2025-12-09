import fileinput
import sys

A=set()
for LINE in fileinput.input():
    X,Y=LINE.rstrip().split(",")
    A.add((int(X),int(Y)))

MAX=0
for A1 in A:
    for A2 in A:
        MAX=max(MAX,abs((A1[0]-A2[0]+1)*(A1[1]-A2[1]+1)))
        print(A1,A2,MAX)

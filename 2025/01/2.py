import fileinput
import sys

POS=50
PWD=0
for line in fileinput.input():
    DELTA=int(line[1:-1])
    if line[0:1]=='L':
        DELTA=-DELTA
        DIR=-1
    else:
        DIR=+1
    # Yes, it's a bit numpty and inefficient, but I can't get it right...
    while (DELTA!=0):
        POS+=DIR
        DELTA-=DIR
        if (POS==100):
            POS=0
        elif (POS==-1):
            POS=99
        if (POS==0):
            PWD+=1
    print(POS, PWD)

import fileinput
import sys

POS=50
PWD=0
for line in fileinput.input():
    DELTA=int(line[1:-1])
    if line[0:1]=='L':
        DELTA=-DELTA
    POS = (POS+DELTA+100)%100
    if POS==0:
        PWD+=1
    print(POS, DELTA, PWD)

import fileinput
import sys

SUM=0
for line in fileinput.input():
    line=line.rstrip()

    # First, find biggest digit starting from right
    FPOS=len(line)-2
    FVAL=0
    i=FPOS
    while (i>=0):
        if int(line[i:i+1]) >= FVAL:
            FPOS=i
            FVAL=int(line[i:i+1])
        i-=1

    # Then, go back to the right and find the biggest digit
    i=FPOS+1
    RVAL=0
    while (i<len(line)):
        if int(line[i:i+1]) >= RVAL:
            RVAL=int(line[i:i+1])
        i+=1

    SUM+=FVAL*10+RVAL
    print(line, FVAL, RVAL, SUM)

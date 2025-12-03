import fileinput
import sys

DIGITS=12
SUM=0
for line in fileinput.input():
    line=line.rstrip()

    FPOS=0 # The position of the previously found digit
    d=DIGITS
    # Loop to find all digits, from the most left to the most right
    while (d>0):
        # Loop to find the biggest digit, as close to the left as possible
        FVAL=0 # The highest digit found so far
        i=len(line)-d
        while (i>=FPOS):
            if int(line[i:i+1]) >= FVAL:
                FVAL=int(line[i:i+1])
                PPOS=i
            i-=1
        FPOS=PPOS+1
        SUM+=FVAL*10**(d-1)
        print(" ",d,FPOS,FVAL,SUM)
        d-=1

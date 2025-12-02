import fileinput
import sys

line=next(fileinput.input())

SUM=0
for RANGE in line[:-1].split(","):
    (START,HYPHEN,END)=RANGE.partition("-")
    print(RANGE,START,END)
    i=START
    while (int(i)<=int(END)):
        HALFLEN=len(i)//2
        if (i == i[:HALFLEN]*2):
            SUM+=int(i)
            print("  ",i,SUM)
        i=str(int(i)+1)

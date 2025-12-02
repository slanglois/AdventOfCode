import fileinput
import sys

line=next(fileinput.input())

def isInvalid(i:str):
    LEN=len(i)//2
    while(LEN>0):
        if (len(i)%LEN==0): # No need to bother otherwise
            if (i == i[:LEN]*(len(i)//LEN)):
                return True
        LEN-=1
    return False

SUM=0
for RANGE in line[:-1].split(","):
    (START,HYPHEN,END)=RANGE.partition("-")
    print(RANGE,START,END)
    I=START
    while (int(I)<=int(END)):
        if (isInvalid(I)):
            SUM+=int(I)
            print("  ",I,SUM)
        I=str(int(I)+1)

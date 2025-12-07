import fileinput
import sys

NBOP=0
SUM=0
I=list()
for line in fileinput.input():
    I.append(line.rstrip("\n"))
    NBOP+=1

print(NBOP,len(I[0]))

NUMBERS=set()
for C in range(len(I[0])-1,-1,-1):
    NUMBER=""
    # Loop per columns, starting with the end
    for L in range(NBOP):
        CHAR=I[L][C]
        if CHAR.isnumeric():
            NUMBER+=CHAR
        elif CHAR=="+":
            NUMBERS.add(NUMBER)
            # Add them all
            S=0
            for N in NUMBERS:
                if N!="": S+=int(N)
            SUM+=S
            print("+",NUMBERS,"=",S,SUM)
            NUMBER=""
            NUMBERS=set()
        elif CHAR=="*":
            NUMBERS.add(NUMBER)
            # Multiply them all
            M=1
            for N in NUMBERS:
                if N!="": M*=int(N)
            SUM+=M
            print("*",NUMBERS,"=",M,SUM)
            NUMBER=""
            NUMBERS=set()
    NUMBERS.add(NUMBER)
    print(NUMBER,NUMBERS)

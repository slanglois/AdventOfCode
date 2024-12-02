import fileinput
import sys

def isSafe(A):
    SAFE=True

    if int(A[0])>int(A[1]):
        RISING=False
    else:
        RISING=True

    for i in range(len(A)-1):
        X=int(A[i])
        Y=int(A[i+1])
        if RISING and X>Y:
            SAFE=False
        if not RISING and X<Y:
            SAFE=False
        if X==Y or abs(X-Y)>3:
            SAFE=False

    print(RISING, A, SAFE)
    return SAFE

S=0
for line in fileinput.input():
    LINE=line.split()
    if isSafe(LINE):
        S+=1
    else:
        for j in range(len(LINE)):
            B=LINE.copy()
            B.pop(j)
            if isSafe(B):
                S+=1
                break
    print(S)

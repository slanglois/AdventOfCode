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
    if isSafe(line.split()):
        S+=1
    print(S)

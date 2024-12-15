import fileinput
import re

number_re=re.compile('p=(.*),(.*) v=(.*),(.*)')

#MAXX=11
#MAXY=7
MAXX=101
MAXY=103
PX=[]
PY=[]
VX=[]
VY=[]

for line in fileinput.input():
    nums=next(number_re.finditer(line))
    PX.append(int(nums.group(1)))
    PY.append(int(nums.group(2)))
    VX.append(int(nums.group(3)))
    VY.append(int(nums.group(4)))
    print(fileinput.lineno(),":",PX,PY,VX,VY)

N=0
FOUND=False
while not FOUND:
    # For each step, store the position of robots in A
    A=set()
    FOUND=True
    for i in range(fileinput.lineno()):
        PX[i]=(PX[i]+VX[i])%MAXX
        PY[i]=(PY[i]+VY[i])%MAXY
        # Apparently, if we have 2 robots on the same place, it's not there yet
        if (PX[i],PY[i]) in A:
            FOUND=False
        else:
            A.add((PX[i],PY[i]))
    N+=1
    print(N)

# Display the bloody tree - maybe
for i in range(MAXY):
    for j in range(MAXX):
      if (j,i) in A: print('X',end="")
      else: print('.',end="")
    print()

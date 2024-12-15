import fileinput
import re

number_re=re.compile('p=(.*),(.*) v=(.*),(.*)')

MAXX=101
MAXY=103
Q1=Q2=Q3=Q4=0
for line in fileinput.input():
    nums=next(number_re.finditer(line))
    PX=int(nums.group(1))
    PY=int(nums.group(2))
    VX=int(nums.group(3))
    VY=int(nums.group(4))
    FX=(PX+100*VX)%MAXX
    FY=(PY+100*VY)%MAXY
    print(fileinput.lineno(),":",PX,PY,VX,VY,"->",FX,FY)
    # Find de quadrant it's in
    if FX==(MAXX-1)//2 or FY==(MAXY-1)//2: continue
    elif FX<MAXX/2:
        if FY<MAXY/2: Q1+=1
        else: Q2+=1
    else:
        if FY<MAXY/2: Q3+=1
        else: Q4+=1
    print(" ",Q1,Q2,Q3,Q4,Q1*Q2*Q3*Q4)

import fileinput
import re

number_re=re.compile('([0-9]*), ..([0-9]*)')

TCOST=0
for line in fileinput.input():
    if line.startswith("Button A"):
        for nums in number_re.finditer(line):
            AX=int(nums.group(1))
            AY=int(nums.group(2))
        print("A",AX,AY)
    elif line.startswith("Button B"):
        for nums in number_re.finditer(line):
            BX=int(nums.group(1))
            BY=int(nums.group(2))
        print("B",BX,BY)
    elif line.startswith("Prize: "):
        for nums in number_re.finditer(line):
            PX=int(nums.group(1))
            PY=int(nums.group(2))
        print("P", PX, PY)
        # That's brute force, but they said 100 iteration max, so that sounds doable!
        FOUND=False
        COST=0
        for ai in range(100):
            for bi in range(100):
                if ai*AX+bi*BX == PX and ai*AY+bi*BY == PY:
                    print(ai,bi,COST)
                    if FOUND:
                        COST=min(3*ai+1*bi, COST)
                    else:
                        COST=3*ai+1*bi
                    FOUND=True
        TCOST+=COST
        print(COST,TCOST)

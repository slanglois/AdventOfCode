import fileinput
import re

# Regexp to match mul(number,number) or do() or don't()
muls_re=re.compile('mul\\(([0-9]*),([0-9]*)\\)|do\\(\\)|don\'t\\(\\)')
S=0
MUL=True
for line in fileinput.input():
    for mul in muls_re.finditer(line):
        # Extract the first 3 chars to know what to do
        match mul.group(0)[0:3]:
            case 'mul':
                if MUL: S+=int(mul.group(1))*int(mul.group(2))
            case 'do(':
                MUL=True
            case 'don':
                MUL=False
        print(mul,S, MUL)

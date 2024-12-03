import fileinput
import re

# Regexp to match mul(number,number)
muls_re=re.compile('mul\\(([0-9]*),([0-9]*)\\)')
S=0
for line in fileinput.input():
    for mul in muls_re.finditer(line):
        S+=int(mul.group(1))*int(mul.group(2))
        print(mul,S)

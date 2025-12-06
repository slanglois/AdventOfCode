import fileinput
import sys

FRESH=0
RANGES=set()
for line in fileinput.input():
    line=line.rstrip()
    # It's a range -> store it
    if ("-" in line):
       RANGES.add(line.partition("-"))
    # It's a number -> test it
    elif line != "":
       for START,_,END in RANGES:
         if int(START)<=int(line)<=int(END):
             FRESH+=1
             print(START,line,END,FRESH)
             break

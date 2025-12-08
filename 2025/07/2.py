import fileinput
import sys

for LINE in fileinput.input():
    LINE=list(LINE.rstrip())
    # We skip the first line, where there's nothing to do
    if fileinput.isfirstline():
        # Replace the S by a 1: now we're counting the timelines for each point
        for I in range(len(LINE)):
          if LINE[I]=="S":
              LINE[I]=1
    else:
        for I in range(len(LINE)):
          if isinstance(UPLINE[I],int):
              if LINE[I]=="^":
                  # Split!
                  if isinstance(LINE[I-1],int):
                      LINE[I-1]+=UPLINE[I]
                  else:
                      LINE[I-1]=UPLINE[I]
                  LINE[I+1]=UPLINE[I]
              else:
                  # Just follow
                  LINE[I]=UPLINE[I]
    print(LINE)
    UPLINE=LINE

SUM=0
for I in LINE:
    if isinstance(I,int):
        SUM+=I
print(SUM)

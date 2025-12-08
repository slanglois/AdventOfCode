import fileinput
import sys

SUM=0
for LINE in fileinput.input():
    LINE=list(LINE.rstrip())
    # We skip the first line, where there's nothing to do
    if not fileinput.isfirstline():
        for I in range(len(LINE)):
          if UPLINE[I]=="S":
              if LINE[I]=="^":
                  # Split!
                  SUM+=1
                  LINE[I-1]="S"
                  LINE[I+1]="S"
              else:
                  # Just follow
                  LINE[I]="S"
    print(LINE, SUM)
    UPLINE=LINE

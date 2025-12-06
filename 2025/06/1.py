import fileinput
import sys

NBOP=0
SUM=0
I=list()
for line in fileinput.input():
    line=line.rstrip()
    I.append(line.split())
    if line.startswith("+") or line.startswith("*"): # This is it!
      for i in range(len(I[0])):
          if (I[NBOP][i]=="*"):
              M=1
              for j in range(NBOP):
                  print("  *",I[j][i])
                  M*=int(I[j][i])
              SUM+=M
              print(i,M,SUM)
          elif (I[NBOP][i]=="+"):
              S=0
              for j in range(NBOP):
                  print("  +",I[j][i])
                  S+=int(I[j][i])
              SUM+=S
              print(i,S,SUM)
          else: print("WTF?")
    NBOP+=1

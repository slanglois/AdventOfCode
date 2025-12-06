import fileinput
import sys

FRESH=0
RANGES=set()
for line in fileinput.input():
    line=line.rstrip()
    # It's a range
    if ("-" in line):
       NEWRANGES=set()
       S1,_,E1=line.partition("-")
       print(S1,E1)
       S1=int(S1)
       E1=int(E1)
       for S,E in RANGES:
           print("  Testing",S,E)
           if E1<=S or E<=S1: # No overlap: just keep this range and carry on
             NEWRANGES.add((S,E))
           elif S1<=S<=E<=E1: # It's already within another range - forget about this range
             pass
           elif S<=S1<=E1<=E: # It's already within another range - keep the bigger one
             S1=S
             E1=E
           elif S1<S<E1<E: # Overlapping on the beginning - change the value and keep the
             E1=E
           elif S<S1<E<E1: # Overlapping on the end
             S1=S
       NEWRANGES.add((S1,E1))
       RANGES=NEWRANGES
       print("->",S1,E1,RANGES)

# Now, we have non-overlapping ranges! Sum their width
SUM=0
for S,E in RANGES:
    SUM+=E-S+1
    print(S,E,SUM)

import fileinput

# Record all antennas ina dict
A=dict()
for line in fileinput.input():
	for i in range(len(line)-1):
		if line[i]!='.':
			if line[i] not in A:
				A[line[i]]=set()
			A[line[i]].add((fileinput.lineno()-1,i))
MAXX=len(line)-1
MAXY=fileinput.lineno()
print(MAXY,MAXX)

ANTINODES=set()

def find_antinode(ANTENNAS: set[tuple[int,int]]) -> None:
	if len(ANTENNAS)==1: return
	else:
		P=ANTENNAS.pop()
		for Q in ANTENNAS:
			# Probably a bit heavy-handed, but simpler to code…
			for i in range(MAXX):
				ANTINODES.add((P[0]-i*(Q[0]-P[0]),P[1]-i*(Q[1]-P[1])))
				ANTINODES.add((Q[0]+i*(Q[0]-P[0]),Q[1]+i*(Q[1]-P[1])))
			print(P,Q)
		find_antinode(ANTENNAS)
		
# Find all antinodes - use recursive function find_antinode()
for FREQ in A:
	print(FREQ)
	find_antinode(A[FREQ])

# Count the ones which are inside the grid
S=0
for P in ANTINODES:
	if 0<=P[0]<MAXY and 0<=P[1]<MAXX: S+=1
print(S)

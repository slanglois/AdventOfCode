import fileinput
import re

def compute_values(LIST):
	if len(LIST)==1:
		return { LIST[0] }
	else:
		NUM=LIST.pop()
		VALS=set()
		for i in compute_values(LIST):
			VALS.add(NUM+i)
			VALS.add(NUM*i)
			VALS.add(int(str(i)+str(NUM)))
		return VALS

S=0
for line in fileinput.input():
	VALUE,REST=line.split(':')
	STROPS=REST[1:-1].split(' ')
	VALUE=int(VALUE)
	OPS=[int(s) for s in STROPS]
	print(VALUE,OPS)

	# Compute all possible values
	POSS_VALS=compute_values(OPS)
	if VALUE in POSS_VALS: S+=VALUE
	print(POSS_VALS, S)

import fileinput
import re

# Recursive function to compute the list of all possible values from a list of numbers
def compute_values(LIST):
	if len(LIST)==1:
	# List of 1 - return a set with the value
		return { LIST[0] }
	else:
	# Call with a list without the last value, and apply it
		NUM=LIST.pop()
		VALS=set()
		for i in compute_values(LIST):
			VALS.add(NUM+i)
			VALS.add(NUM*i)
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

BEGIN { FS="," }

{ A[$1,$2,$3]=1 }

END {
	# Initialise to the number of free sides
	S=NR*6;
	# Loop over each cell
	for (CELL in A) {
		# awk hacky way of looping over multidimensional arrays…
		split(CELL, X, SUBSEP);
		if (A[X[1],X[2],X[3]]==0) continue;
		# Test each of the 6 adjacent cells. If it is not empty, remove 1 to the result
		if (A[X[1]+1,X[2],X[3]]==1) S--;
		if (A[X[1],X[2]+1,X[3]]==1) S--;
		if (A[X[1],X[2],X[3]+1]==1) S--;
		if (A[X[1]-1,X[2],X[3]]==1) S--;
		if (A[X[1],X[2]-1,X[3]]==1) S--;
		if (A[X[1],X[2],X[3]-1]==1) S--;
		print S;
	}
	print S;
}

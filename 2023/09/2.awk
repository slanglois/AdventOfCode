{
	print;
	# Store all numbers in the first line of a table
	delete A;
	for (i=1; i<=NF; i++) A[0,i]=$i;

	# Look for all zeroes
	DEPTH=0;
	do {
		DEPTH++;
		ALLZEROES=1;
		for (i=1; i<=(NF-DEPTH); i++) {
			A[DEPTH,i]=A[DEPTH-1,i+1]-A[DEPTH-1,i];
			if (A[DEPTH,i]!=0) ALLZEROES=0;
			printf A[DEPTH,i]" ";
		}
		print "";
	} while (!ALLZEROES)

	# Compute the first number at each depth
	A[0,DEPTH]=0;
	for (i=DEPTH-1; i>=0; i--) A[i,0]=A[i,1]-A[i+1,0];
	S+=A[0,0];
	print "N", A[0,0],"Sum",S;
}

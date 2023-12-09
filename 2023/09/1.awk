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

	# Add the last number of each depth
	for (i=0; i<=DEPTH; i++) S+=A[i,NF-i];
	print "Sum",S;
}

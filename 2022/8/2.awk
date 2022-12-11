{
	for (i=1; i<=length($1); i++) A[NR,i]=substr($1,i,1)
}
END {
	for (i=1; i<=NR; i++) for (j=1; j<=NR; j++) {
		SCORE=1

		# To West
		DIST=1
		for (k=j-1; k>0 && A[i,k]<A[i,j] ; k--) {
			DIST++
		}
		if (k==0) DIST--;
		printf i j " " DIST;
		SCORE*=DIST;

		# To North
		DIST=1
		for (k=i-1; k>0 && A[k,j]<A[i,j] ; k--) {
			DIST++
		}
		if (k==0) DIST--;
		printf " " DIST;
		SCORE*=DIST;

		# To East
		DIST=1
		for (k=j+1; k<=NR && A[i,k]<A[i,j] ; k++) {
			DIST++
		}
		if (k==NR+1) DIST--;
		printf " " DIST;
		SCORE*=DIST;

		# To South
		DIST=1
		for (k=i+1; k<=NR && A[k,j]<A[i,j] ; k++) {
			DIST++
		}
		if (k==NR+1) DIST--;
		printf " " DIST;
		SCORE*=DIST;

		print " " SCORE

		if (SCORE > HIGHSCORE) HIGHSCORE=SCORE
	}
	print HIGHSCORE
}

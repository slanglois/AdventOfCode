{
	for (i=1; i<=length($1); i++) A[NR,i]=substr($1,i,1)
}
END {
	print " From West"
	for (i=1; i<=NR; i++) {
		S=-1;
		for (j=1; j<=NR; j++) {
			if (A[i,j]>S) { S=A[i,j]; B[i,j]=1; print i,j }
		}
	}
	print " From North"
	for (j=1; j<=NR; j++) {
		S=-1;
		for (i=1; i<=NR; i++) {
			if (A[i,j]>S) { S=A[i,j]; B[i,j]=1; print i,j }
		}
	}
	print " From East"
	for (i=1; i<=NR; i++) {
		S=-1;
		for (j=NR; j>0; j--) {
			if (A[i,j]>S) { S=A[i,j]; B[i,j]=1; print i,j }
		}
	}
	print " From West"
	for (j=1; j<=NR; j++) {
		S=-1;
		for (i=NR; i>0; i--) {
			if (A[i,j]>S) { S=A[i,j]; B[i,j]=1; print i,j }
		}
	}

	for (i=1; i<=NR; i++) for (j=1; j<=NR; j++) SUM+=B[i,j]
	print "Final count:" SUM
}

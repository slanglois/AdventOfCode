{ A[NR]=$1; B[NR]=$2 }
END {
	for(i=1; i<NR+1; i++) {
		# Not super efficient, but good enough…
		for (j=1; j<NR+1; j++)
			if(A[i]==B[j]) S+=A[i]
		print A[i],S
	}
}

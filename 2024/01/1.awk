{ A[NR]=$1; B[NR]=$2 }
END {
	asort(A);
	asort(B);
	for(i=1; i<NR+1; i++) {
		D=A[i]-B[i];
		if (D>0) S+=D; else S-=D; # No abs() function in awk!
		print A[i],B[i],D,S
	}
}

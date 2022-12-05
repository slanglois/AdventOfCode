function move(nb,source,dest) {
	for (n=nb; n>=1; n--) {
		LENGTH[dest]++;
		B[dest,LENGTH[dest]]=B[source,LENGTH[source]-n+1];
	}
	LENGTH[source]-=nb;
	for (s=1; s<=NB; s++ ) printf "%s",B[s,LENGTH[s]]
	print ""
}

BEGIN {
	NB=split (ALLBOXES, STACK, " ")
	for (s=1; s<=NB; s++ ) {
		print STACK[s]
		LENGTH[s]=length(STACK[s]); 
		for (i=1; i<=LENGTH[s]; i++) { B[s,i]=substr(STACK[s],i,1)}
	}
}
/move / { move($2,$4,$6) }

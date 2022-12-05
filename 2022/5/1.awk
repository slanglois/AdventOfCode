function move(source,dest) {
	LENGTH[dest]++;
	B[dest,LENGTH[dest]]=B[source,LENGTH[source]];
	LENGTH[source]--;
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
/move / { for (i=1; i<=$2; i++) move($4,$6) }

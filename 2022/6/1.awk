BEGIN { MAX=14 }
{
	for (i=1+MAX; i<=length($1); i++) {
		print "Testing " substr($1,i-MAX,MAX);
		for (j=i-MAX; j<i; j++) { OCC[substr($1,j,1)]=1; print substr($1,j,1) }
		print length(OCC);
		if (length(OCC)==MAX) { print i-1; next }
		delete OCC
	}
}

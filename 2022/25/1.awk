# For ease of processing, consider each character as a field
BEGIN { FS="" }

{
	N=0;
	for(i=1; i<=NF; i++) {
		if ($i=="=") N-=2*5^(NF-i)
		else if ($i=="-") N-=5^(NF-i)
		else N+=$i*5^(NF-i)
	}
	SUM+=N
}

END {
	print SUM;
	# Build up SNAFU number by looking at the number mod 5, computing smallest digit first
	while (SUM > 0) {
		DIGIT=SUM%5;
		# print SUM,DIGIT
		if (DIGIT==4) { SNAFU="-" SNAFU; SUM+=1 }
		else if (DIGIT==3) { SNAFU="=" SNAFU; SUM+=2 }
		else { SNAFU=DIGIT SNAFU; SUM-=DIGIT }
		# SUM should now be a multiple of 5
		SUM=SUM/5;
	}
	print SNAFU
}

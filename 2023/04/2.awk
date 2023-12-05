BEGIN {
	# Initialises number of copies for each card. We don't know yet how many there are, so pick an arbitrary big number
	for (i=1; i<=1000; i++) COPIES[i]=1;
}
 
# Main loop
{
	print "Card",NR;
	MODE=0;
	SCORE=0;
	for (i=3; i<=NF; i++) {
		if ($i=="|") MODE=i;
		else if (MODE==0) WINNING[i]=$i;
			else {
				for (j=3; j<=MODE; j++) {
					# print "Looking at ", $i, j, WINNING[j];
					if ($i==WINNING[j]) SCORE++;
				}
			}
	}
	#Now, increment the copies for the next cards
	for (i=NR+1; i<=NR+SCORE; i++) COPIES[i]+=COPIES[NR];
	print "Adding",COPIES[NR],"to the next",SCORE,"cards";
}
 
END {
	# Finally, compute total number of copies
	for (i=1; i<=NR; i++) {
		print "Copies of",i,COPIES[i];
		S+=COPIES[i];
	}
	print S
}

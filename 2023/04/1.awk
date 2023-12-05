{
	print "Card",NR;
	MODE=0;
	SCORE=0;
	for (i=3; i<=NF; i++) {
		if ($i=="|") MODE=i;
		else if (MODE==0) WINNING[i]=$i;
			else for (j=3; j<=MODE; j++) {
				# print "Looking at ", $i, j, WINNING[j];
				if ($i==WINNING[j]) {
					if (SCORE==0) SCORE=1; else SCORE*=2;
					print "Found one", $i, SCORE
				}
			}
	}
	S+=SCORE;
}
 
END {print S}

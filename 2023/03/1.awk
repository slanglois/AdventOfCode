BEGIN { FS="" }

# Just record everything into an array
{
	for (i=1; i<=NF; i++) A[i,NR]=$i
	# Initialise both ends with dots - makes it easier later
	A[0,NR]="."
	A[NF+1,NR]="."
}

END {
	# Add top and bottom lines with dots as well
	for (i=0; i<=NF+1; i++) {
		A[i,0]=".";
		A[i,NR+1]=".";
	}

#	for (LINE=0; LINE<=NR+1; LINE++) {
#		for (COL=NF+1; COL>=0; COL--) printf A[COL,LINE]
#		print ""
#	}

	N=0;
	POWER=0;
	# Loop over each cell - from the end, so we can just add digits to the number
	for (LINE=1; LINE<=NR; LINE++) {
		for (COL=NF+1; COL>=0; COL--) {
			if (A[COL,LINE] ~ /[0-9]/) {
				if (POWER==0) {
					# We're starting to read a number. Initialise all the things!
					POWER=1;
					COLSTART=COL;
					N=A[COL,LINE];
					print "Start number", N, COLSTART;
				} else {
					# We're continuing a number. Keep adding
					POWER*=10;
					N+=A[COL,LINE]*POWER;
				}
			} else {
				if (POWER==0) {
					# Nothing to do there, we're just reading non-numbers
				} else {
					# We've just finished a number. Let's get to work…
					print "End number", N, COL, COLSTART;
					# Is it next to a symbol on the same line?
					if ((A[COL,LINE] !~ /[0-9\.]/) || (A[COLSTART+1,LINE] !~ /[0-9\.]/)) {
						S+=N;
						print "Found one!", N, S;
					# Is it next to a symbol on the next or previous line?
					} else for (c=COL; c<=COLSTART+1; c++) {
						if ((A[c,LINE-1] !~ /[0-9\.]/) || (A[c,LINE+1] !~ /[0-9\.]/)) {
							S+=N;
							print "Found one!", N, S;
							break;
						}
					}
					N=0;
					POWER=0;
				}
			}
		}
	}
}

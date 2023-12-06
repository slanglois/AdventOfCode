/seeds:/ {
	# Store seeds batch numbers
	for (i=2; i<=NF; i+=2) {
		SEEDS[i]=$i;
		SEEDRANGE[i]=$(i+1);
	}
}
 
/map:/ {
	# Just store which step (soil, etc.) we're storing now
	STEP++;
	print "Storing step",STEP,$1
}
 
/^[0-9]/ {
	# Just store the 3 values, we'll deal with them later
	SOUR[STEP,NR]=$2;
	DEST[STEP,NR]=$1;
	RANG[STEP,NR]=$3;
}
 
END {
	LOWESTLOCATION=9999999999999;
	for (SEEDID in SEEDS) {
		print "Seed batch"SEEDS[SEEDID],SEEDRANGE[SEEDID];
		for (SEED=SEEDS[SEEDID]; SEED<SEEDS[SEEDID]+SEEDRANGE[SEEDID]; SEED++) {
			STEP=1;
			BATCHID=SEED;
			# print "Seed",BATCHID;

			# Loop over each 7 steps: soil, etc.
			for (STEP=1; STEP<=7; STEP++) {
				NEXTBATCHID=0;
				# Look in all the maps which one fits that Step + BatchId
				for (ID in SOUR) {
					# Check we're on the right step and the range matches
					if (substr(ID,1,1)==STEP && (BATCHID>=SOUR[ID]) && (BATCHID<(SOUR[ID]+RANG[ID]))) {
						NEXTBATCHID=BATCHID+DEST[ID]-SOUR[ID];
						# print "  Found a match!", SOUR[ID], DEST[ID], RANG[ID], "->", NEXTBATCHID;
						break;
					}
				}
				# Didn't find a match: default is keep the same BatchId
				if (NEXTBATCHID>0) BATCHID=NEXTBATCHID;
				# print "  Step",STEP,BATCHID;
			}
			if (BATCHID<LOWESTLOCATION) {
				LOWESTLOCATION=BATCHID;
				print "Lowest found for seed",SEED, ":", LOWESTLOCATION;
			}
		}
	}
}

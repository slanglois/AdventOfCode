/Time:/ { for (i=2; i<=NF; i++) TIME[i]=$i }
/Distance:/ { for (i=2; i<=NF; i++) DISTANCE[i]=$i }

END {
	MULT=1;
	for (RACE in TIME) {
		NBWAYS=0;
		print "Race", TIME[RACE], DISTANCE[RACE];
		for (HOLD=1; HOLD<TIME[RACE]; HOLD++) {
			FINISHINGDISTANCE=HOLD*(TIME[RACE]-HOLD);
			if (FINISHINGDISTANCE>DISTANCE[RACE]) {
				NBWAYS++;
				print "  Found another record: ", FINISHINGDISTANCE, HOLD, NBWAYS;
			}
		}
		MULT*=NBWAYS;
	}
	print MULT
}

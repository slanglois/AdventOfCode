# Need to play with types here, to get the numbers concatenated
/Time:/ { for (i=2; i<=NF; i++) TIME=""TIME$i; TIME=TIME+0 }
/Distance:/ { for (i=2; i<=NF; i++) DISTANCE=""DISTANCE$i; DISTANCE=DISTANCE+0}

# Looks horrendously long, but actually takes 2 seconds!
END {
	print "Race", TIME, DISTANCE;
	for (HOLD=1; HOLD<TIME; HOLD++) {
		FINISHINGDISTANCE=HOLD*(TIME-HOLD);
		if (FINISHINGDISTANCE>DISTANCE) NBWAYS++;
	}
	print NBWAYS
}

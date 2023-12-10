BEGIN { FS="" }

{
	# Just store everything
	for (i=1; i<=NF; i++) {
		A[i,NR]=$i;
		if ($i=="S") { # Found the bloody S!
			SX=i; SY=NR; print "S in",SX,SY;
		}
	}
	
}

END {
	# We need to find out what's under the S by looking at its surrounding
	if (A[SX,SY-1] ~ /[|7F]/) NORTH=1;
	if (A[SX,SY+1] ~ /[|LJ]/) SOUTH=1;
	if (A[SX-1,SY] ~ /[-FL]/) WEST=1;
	if (A[SX+1,SY] ~ /[-J7]/) EAST=1;
	print NORTH, SOUTH, WEST, EAST;
	if (NORTH==1) {
		if (SOUTH==1) A[SX,SY]="|"
		else if (EAST==1) A[SX,SY]="L"
		else if (WEST==1) A[SX,SY]="J"
	} else if (SOUTH==1) {
		if (EAST==1) A[SX,SY]="F"
		else if (WEST==1) A[SX,SY]="7"
	} else if (EAST==1)
		if (WEST==1) A[SX,SY]="-"
	print "Under the S is a",A[SX,SY];	

	# Now, follow the path until we are in the same position
	X=SX; Y=SY; # Starting position
	PX=PY=0; # Store previous position, so we don't go backwards!
	STEPS=0;
	do {
		STEPS++;
		NORTH=SOUTH=EAST=WEST=0;
		if (A[X,Y] ~ /[|7F]/) SOUTH=1;
		if (A[X,Y] ~ /[|LJ]/) NORTH=1;
		if (A[X,Y] ~ /[-FL]/) EAST=1;
		if (A[X,Y] ~ /[-J7]/) WEST=1;
		     if ((NORTH==1) && ((PX!=X) || (PY!=Y-1))) { PX=X; PY=Y; Y--; print "NORTH",STEPS,X,Y; }
		else if ((SOUTH==1) && ((PX!=X) || (PY!=Y+1))) { PX=X; PY=Y; Y++; print "SOUTH",STEPS,X,Y; }
		else if ((WEST==1) && ((PX!=X-1) || (PY!=Y))) { PX=X; PY=Y; X--; print "WEST",STEPS,X,Y; }
		else if ((EAST==1) && ((PX!=X+1) || (PY!=Y))) { PX=X; PY=Y; X++; print "EAST",STEPS,X,Y; }
	} while ((X!=SX) || (Y!=SY))
	print "Done!", STEPS/2;
}

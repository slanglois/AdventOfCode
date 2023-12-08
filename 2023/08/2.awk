{ # Just store the map
	if (NR==1) for (i=1; i<=length($0); i++) MAP[i]=substr($0,i,1);
}
 
/=/ { # Just store the paths
	LEFT[$1]=substr($3,2,3);
	RIGHT[$1]=substr($4,1,3);
}
 
END {
	# Find out the ghosts we need
	for (p in LEFT) if (substr(p,3,1)=="A") GHOST[p]=p;
 
	# Compute the cycle number for each ghost
	for (g in GHOST) {
		print GHOST[g];
		NBSTEP[g]=0;
		MAPSTEP=1;
		while (substr(GHOST[g],3,1)!="Z") {
			if (MAP[MAPSTEP]=="L") GHOST[g]=LEFT[GHOST[g]]; else GHOST[g]=RIGHT[GHOST[g]];
			NBSTEP[g]++;
			MAPSTEP++;
			if (MAPSTEP>length(MAP)) MAPSTEP=1;
		}
		print "Step",NBSTEP[g]
	}

	# Find out the smallest common multiple for these numbers
	STEPS=1;
	for (g in GHOST) {
		STEPS=SCM(STEPS,NBSTEP[g]);
		print STEPS;
	}
}

# Greatest Common Divisor
function GCD(A,B) {
	while (B!=0) {
		T=B;
		B=A%B;
		A=T;
	}
	return A;
}

# Smallest Common Multiple
function SCM(A,B) {
	return A/GCD(A,B)*B;
}

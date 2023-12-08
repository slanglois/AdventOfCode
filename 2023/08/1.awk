{ # Just store the map
	if (NR==1) for (i=1; i<=length($0); i++) MAP[i]=substr($0,i,1);
}
 
/=/ { # Just store the paths
	LEFT[$1]=substr($3,2,3);
	RIGHT[$1]=substr($4,1,3);
}
 
END {
	POS="AAA";
	NBSTEP=0;
	MAPSTEP=1;
	while (POS!="ZZZ") {
		if (MAP[MAPSTEP]=="L") POS=LEFT[POS]; else POS=RIGHT[POS];
		NBSTEP++;
		MAPSTEP++;
		if (MAPSTEP>length(MAP)) MAPSTEP=1;
		print "Pos",POS,"Step",NBSTEP,"Map",MAPSTEP;
	}
}

BEGIN {
	FS=",";
	# awk is quite poor, so we need to build an table of ASCII char
	for (i=1; i<256; i++) ASCII[sprintf("%c",i)]=i
}

{
	for (i=1; i<=NF; i++) {
		if (substr($i,length($i))=="-") {
		# Let's remove a lens
			LENS=substr($i,1,length($i)-1);
			BOX=Hash(LENS)
			print "Removing",LENS,"in box",BOX;
			for (j=1; j<=length(BOXES[BOX]); j++) {
				if (LENS==substr(BOXES[BOX][j],1,length($i)-1)) {
					print "Removed in place",j;
					# Shift all the following lenses
					for (k=j; k<=length(BOXES[BOX])-1; k++) {
						BOXES[BOX][k]=BOXES[BOX][k+1];
					}
					# and delete the last element
					delete BOXES[BOX][length(BOXES[BOX])];
				}
			}
		} else {
			LENS=substr($i,1,length($i)-2);
			BOX=Hash(LENS)
			print "Adding",LENS,"in box",BOX;
			FOUND=0;
			for (j=1; j<=length(BOXES[BOX]); j++) {
				if (LENS==substr(BOXES[BOX][j],1,length($i)-2)) {
					print "  Found it in place",j;
					FOUND=1;
					BOXES[BOX][j]=$i;
					break;
				}
			}
			if (FOUND==0) {
				print "  Adding it in place",length(BOXES[BOX])+1;
				BOXES[BOX][length(BOXES[BOX])+1]=$i;
			}
		}
	}
}

END {
	# Just need to compute the sum now
	for (i=0; i<=256; i++) {
		SUMBOX=0;
		for (j=1; j<=length(BOXES[i]); j++) {
			BOX=(i+1)*j*substr(BOXES[i][j],length(BOXES[i][j]));
			print "Box",i,"pos",j,"sum",BOX;
			SUMBOX+=BOX;
		}
		SUM+=SUMBOX;
		print "Box",i,"Sum",SUMBOX,"Total",SUM;
	}
	
}

function Hash(S) {
	HASH=0;
	for (c=1; c<=length(S); c++) {
		HASH+=ASCII[substr(S,c,1)];
		HASH*=17;
		HASH%=256;
	}
	return HASH;
}

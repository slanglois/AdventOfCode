BEGIN { FS="" }

# Just store each cell in A
{
	for (i=1; i<=NF; i++) A[i,NR]=$i;
}

END {
for (ENTRY=1; ENTRY<=2*(NR+NF); ENTRY++) {
	# We initialize a stack of where each beam is, and which direction. 
	delete B;
	delete LIT;
	if (ENTRY<=NR) B[1,ENTRY,">"]=1
	else if (ENTRY<=NR+NF) B[ENTRY-NR,1,"v"]=1
	else if (ENTRY<=2*NR+NF) B[NF,ENTRY-NR-NF,"<"]=1
	else B[ENTRY-2*NR-NF,NR,"^"]=1

	# There are probably cycles in the beams… Loop enough time so we find everything
	for (STEPS=1; STEPS<2000; STEPS++) {
	for (POS in B) {
		# Extract coordinates
		split(POS, COORD, SUBSEP)
		X=COORD[1];
		Y=COORD[2];
		DIR=COORD[3];

		# Light the cell, and delete it from the stack
		LIT[X,Y]=1;
		delete B[POS];

		# print X,Y,DIR,A[X,Y],STEPS,length(LIT);

		switch (DIR) {
		case ">": 
			switch (A[X,Y]) {
			case ".":
			case "-":
				if (X<NF) B[X+1,Y,">"]=1;
				break;
			case "/":
				if (Y>1) B[X,Y-1,"^"]=1;
				break;
			case "\\":
				if (Y<NR) B[X,Y+1,"v"]=1;
				break;
			case "|":
				if (Y>1) B[X,Y-1,"^"]=1;
				if (Y<NR) B[X,Y+1,"v"]=1;
				break;
			default: print "ERROR!",X,Y,DIR,A[X,Y]; exit;
			}
			break

		case "<": 
			switch (A[X,Y]) {
			case ".":
			case "-":
				if (X>1) B[X-1,Y,"<"]=1;
				break
			case "\\":
				if (Y>1) B[X,Y-1,"^"]=1;
				break
			case "/":
				if (Y<NR) B[X,Y+1,"v"]=1;
				break
			case "|":
				if (Y>1) B[X,Y-1,"^"]=1;
				if (Y<NR) B[X,Y+1,"v"]=1;
				break
			default: print "ERROR!",X,Y,DIR,A[X,Y]; exit;
			}
			break

		case "^": 
			switch (A[X,Y]) {
			case ".":
			case "|":
				if (Y>1) B[X,Y-1,"^"]=1;
				break
			case "\\":
				if (X>1) B[X-1,Y,"<"]=1;
				break
			case "/":
				if (X<NF) B[X+1,Y,">"]=1;
				break
			case "-":
				if (X>1) B[X-1,Y,"<"]=1;
				if (X<NF) B[X+1,Y,">"]=1;
				break
			default: print "ERROR!",X,Y,DIR,A[X,Y]; exit;
			}
			break

		case "v": 
			switch (A[X,Y]) {
			case ".":
			case "|":
				if (Y<NR) B[X,Y+1,"v"]=1;
				break
			case "\\":
				if (X<NR) B[X+1,Y,">"]=1;
				break
			case "/":
				if (X>1) B[X-1,Y,"<"]=1;
				break
			case "-":
				if (X>1) B[X-1,Y,"<"]=1;
				if (X<NR) B[X+1,Y,">"]=1;
				break
			default: print "ERROR!",X,Y,DIR,A[X,Y]; exit;
			}
			break

		default: print "ERROR!",X,Y,DIR; exit;
		} # switch DIR
		# DEBUG: print list of positions
#		for (POS2 in B) print "   ",POS2;
	} # for (POS in B)
	} # for (STEPS)
	if (MAXLIT<length(LIT)) MAXLIT=length(LIT);
	print length(LIT),MAXLIT;
} # for ENTRY
}

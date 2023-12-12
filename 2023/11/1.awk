BEGIN {FS=""}
 
{ # Just store the map
	for (i=1; i<=NF; i++) A[i,NR]=$i;
}
 
END {
	for (j=1; j<=NR; j++) {
		for (i=1; i<=NF; i++) { printf A[i,j] }
		print ""
	}

	# First, find out which rows and columns are empty
	for (j=1; j<=NR; j++) {
		ISEMPTY=1;
		for (i=1; i<=NF; i++) {
			if (A[i,j]=="#") { ISEMPTY=0; break }
		}
		EMPTY[j,0]=ISEMPTY;
		print "Row", j, ISEMPTY;
	}
	for (i=1; i<=NF; i++) {
		ISEMPTY=1;
		for (j=1; j<=NR; j++) {
			if (A[i,j]=="#") { ISEMPTY=0; break }
		}
		EMPTY[0,i]=ISEMPTY;
		print "Line", i, ISEMPTY;
	}

	# Let's go! First, find a galaxy
	for (GJ=1; GJ<=NR; GJ++) {
		for (GI=1; GI<=NF; GI++) {
			if (A[GI,GJ]=="#") {
				# Now find another, and compute the distance
				for (j=1; j<=NR; j++) for (i=1; i<=NF; i++) if (A[i,j]=="#") {
					DISTANCE=abs(GJ,j)+abs(GI,i);
					# We don't "expand" the universe, we just add more distance for each empty row/line
					for (x=min(GI,i)+1; x<max(GI,i); x++) if (EMPTY[0,x]) DISTANCE++;
					for (x=min(GJ,j)+1; x<max(GJ,j); x++) if (EMPTY[x,0]) DISTANCE++;
					TOTAL+=DISTANCE;
					print "Galaxies",GI,GJ,"and",i,j,"Distance",DISTANCE,"Total",TOTAL;
				}
			}
		}
	}
	print TOTAL/2;
}
 
function abs(A,B) { if (A<B) return B-A; return A-B }
function min(A,B) { if (A<B) return A; return B }
function max(A,B) { if (A<B) return B; return A }

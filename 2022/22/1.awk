BEGIN { FS=""; print "Reading map..." }

/\./ {
	# Record map - and store max number of columns
	for(i=1;i<=length($0); i++) {
		A[i,NR]=$i;
		if(i>MAXCOL) MAXCOL=i
	}
}

/^$/ {
	
	# Initialise all the variables
	FS=" "
	DIR=0
	ROW=1
	MAXROW=NR-1
	# Looking for starting point
	for (i=1;i<=MAXCOL; i++)
		if(A[i,1]==".") { COL=i; break }
	print "Starting in (",ROW,COL,") in a map of (",MAXROW,MAXCOL,")"
	for(i=1;i<=MAXROW; i++) {
		for(j=1;j<=MAXCOL;j++) printf A[i,j]
		print
	}
}

# Turn right
/^R$/ { DIR++; DIR%=4; printpos() }

# Turn left
/^L$/ { DIR--; DIR%=4; printpos() }

# Move forward
/^[0-9]*$/ {
	print "Line is",$1
	for(j=1;j<=$1;j++) {
		if (DIR==0) {
			if(A[COL+1,ROW]=="#") break;
			else if(A[COL+1,ROW]==".") COL++;
			else if(A[COL+1,ROW]=="")
				for (i=1;i<=MAXCOL; i++)
					if(A[i,ROW]==".") { COL=i; break }
		}
		else if (DIR==1) {
			if(A[COL,ROW+1]=="#") break
			else if(A[COL,ROW+1]==".") ROW++
			else if(A[COL,ROW+1]=="")
				for (i=1;i<=MAXROW; i++)
					if(A[COL,i]==".") { ROW=i; break }
		}
		else if (DIR==2) {
			if(A[COL-1,ROW]=="#") break;
			else if(A[COL-1,ROW]==".") COL--;
			else if(A[COL-1,ROW]=="")
				for (i=MAXCOL;; i--)
					if(A[i,ROW]==".") { COL=i; break }
		}
		else if (DIR==3) {
			if(A[COL,ROW-1]=="#") break;
			else if(A[COL,ROW-1]==".") ROW++;
			else if(A[COL,ROW-1]=="")
				for (i=MAXROW;; i--)
					if(A[COL,i]==".") { ROW=i; break }
		}
		printpos()
	}
}

function printpos() {
	print "Now in (",ROW,COL,") with a dir of ",DIR
}

{ A[NR]=$1 }
END {
	for (i=1; i<NR; i++) printf A[i] " "
	print
	for (INDEX=1; INDEX<NR; INDEX++) {
		NUM=A[INDEX];
		if (NUM>0)
			for (i=0; i<NUM; i++) move(INDEX+i,1)
		else if (NUM<0)
			for (i=0; i>NUM; i--) move(INDEX+i,-1)
		for (i=1; i<NR; i++) printf A[i] " "
		print
	}
}

function move(j, dir) {
	print "move" j dir INDEX
	temp=A[j+dir];
	A[j+dir]=A[j];
	A[j]=temp;
	if (INDEX==j) INDEX-=dir
}

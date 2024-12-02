{
	SAFE=1;
	# Going up or down?
	if ($2>$1) C=1; else C=0;
	for (i=1; i<NF; i++) {
		if (C==1) if ($i>$(i+1)) SAFE=0;
		if (C==0) if ($(i+1)>$i) SAFE=0;
		if ($(i+1)-$i>3 || $(i+1)-$i<-3 || $i==$(i+1)) SAFE=0
		print C,$i,$(i+1),SAFE;
	}
	S+=SAFE;
	print SAFE, S
}

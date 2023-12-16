BEGIN {
	FS=",";
	# awk is quite poor, so we need to build an table of ASCII char
	for (i=1; i<256; i++) ASCII[sprintf("%c",i)]=i
}

{
	for (i=1; i<=NF; i++) {
		HASH=0;
		for (c=1; c<=length($i); c++) {
			HASH+=ASCII[substr($i,c,1)];
			HASH*=17;
			HASH%=256;
		}
		SUM+=HASH;
		print $i, HASH, SUM;
	}
}

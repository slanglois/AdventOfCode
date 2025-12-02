BEGIN { FS="," }
{
	# Iterate over ranges
	for (i=1; i<=NF; i++) {
		split($i,RANGE,"-")
		print $i,RANGE[1],RANGE[2]
		# Iterate over all values in the range
		for (j=RANGE[1]; j<=RANGE[2]; j++) {
			HALFLEN=int(length(j)/2)
			if (j==(substr(j,1,HALFLEN) substr(j,1,HALFLEN))) {
				SUM+=j; print " ",j,SUM
			}
		}
	}
}

BEGIN { FS="" }
 
{
	# Find first digit and adds it to S
	for (i=1;i<=NF;i++) {
		CHAR=substr($0,i,1);
		printf "%s ", CHAR
		if (CHAR ~ /[0-9]/) {
			S+=CHAR*10;
			break;
		}
	}

	# Find last digit and adds it to S
	for (i=NF;i>=1;i--) {
		CHAR=substr($0,i,1);
		printf "%s ", CHAR
		if (CHAR ~ /[0-9]/) {
			S+=CHAR;
			break;
		}
	}
	print $0, S
}
 
END { print S }

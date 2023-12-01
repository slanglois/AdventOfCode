BEGIN {
	FS="";
	# Initialise array of numbers - best way in awk!
	split("one!two!three!four!five!six!seven!eight!nine",NUMBERS,"!");
}

function IsDigitFirst(S) {
	CHAR=substr(S,0,1);
	if (CHAR ~ /[0-9]/) return CHAR;

	for (n=1;n<10;n++) {
		if (substr(S,0,length(NUMBERS[n]))==NUMBERS[n]) return n;
	}
	return 0
}

function IsDigitLast(S) {
	CHAR=substr(S,length(S),1);
	if (CHAR ~ /[0-9]/) return CHAR;

	for (n=1;n<10;n++) {
		#print "------- looking for",n,"in",S,":",substr(S,length(S)-length(NUMBERS[n])+1)
		if (substr(S,length(S)-length(NUMBERS[n])+1)==NUMBERS[n]) return n;
	}
	return 0
}

# Main loop
{
	print

	# Find first digit and adds it to S
	for (i=1;i<=NF;i++) {
		F=IsDigitFirst(substr($0,i));
		if (F>0) {
			print "Found first digit:", F;
			S+=F*10
			break;
		}
	}

	# Find last digit and adds it to S
	for (i=NF;i>=1;i--) {
		F=IsDigitLast(substr($0,0,i));
		if (F>0) {
			print "Found last digit:", F;
			S+=F
			break;
		}
	}
	print "S =", S
}
 
END { print S }

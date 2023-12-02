BEGIN {
	# We don't really care about punctuation here
	FS="[ ,;:]*";

	# Initialise max for each colour
	MAX["red"]=12;
	MAX["green"]=13;
	MAX["blue"]=14;
}

# Main loop
{
	GAME=$2;
	print "Game", GAME;
	for (i=3; i<NF; i+=2) {
		COLOUR=$(i+1);
		if ($i>MAX[COLOUR]) {
			print "  Stopping because",COLOUR,"=",$i;
			next;
		}
	}
	S+=GAME
	print "S", S
}

END { print S }

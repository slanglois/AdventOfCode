BEGIN {
	# We don't really care about punctuation here
	FS="[ ,;:]*";
}

# Main loop
{
	# reinitialise max for each colour
	MAX["red"]=0;
	MAX["green"]=0;
	MAX["blue"]=0;

	GAME=$2;
	print "Game", GAME;
	for (i=3; i<NF; i+=2) {
		COLOUR=$(i+1);
		if ($i>MAX[COLOUR]) {
			MAX[COLOUR]=$i;
		}
	}
	S+=MAX["red"]*MAX["green"]*MAX["blue"]
	print "S", S
}

END { print S }

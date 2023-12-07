# This will just add a digit in front of the first field depending on the type of hand
# 6 -> 5 of a kind; 5 -> 4 of a kind; 4 -> Full house, etc.
# Use it like this:
# cat sample.txt | awk -f 1-prependtype.awk  | tr 'AKQJT' 'ZYXWV' | sort | awk '{S+=NR*$3} END {print S}'

BEGIN { FS="" }
 
{
        delete CARD;
        # Count number of each card
        for (i=1; i<=5; i++) CARD[$i]++;
        # Sort and decide type from number of most frequent card
        asort(CARD);
        switch (CARD[length(CARD)]) {
                case 5: TYPE=6; break # 5 of a kind
                case 4: TYPE=5; break # 4 of a kind
                case 3: if (CARD[1]==2) TYPE=4 # Full house
                        else TYPE=3 # 3 of a kind
                        break
                case 2: if (CARD[2]==2) TYPE=2 # Double pairs
                        else TYPE=1 # Single pair
                        break
                case 1: TYPE=0; break # High card
                default: print "IMPOSSIBLE!"
        }
        print TYPE,$0;
}

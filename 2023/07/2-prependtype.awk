# This will just add a digit in front of the first field depending on the type of hand
# 6 -> 5 of a kind
# 5 -> 4 of a kind
# 4 -> Full house
# 3 -> 3 of a kind
# 2 -> Double pair
# 1 -> Pair
# 0 -> High card
# Use it like this:
# cat input.txt | awk -f 2-prependtype.awk | tr 'AKQJT' 'ZYX0V' | sort | awk '{S+=NR*$3} END {print S}'

{
        TYPE=FindType($1);
        print TYPE,$0;
}
 
function FindType(HAND) {
        delete CARD;
        # Count number of each card
        for (i=1; i<=5; i++) CARD[substr(HAND,i,1)]++;
        # for (C in CARD) print "Card", C, ",", CARD[C];
        asort(CARD,SORTEDCARD);
        NBJ=CARD["J"]; # number of Jokers
        switch (SORTEDCARD[length(SORTEDCARD)]) {
                case 5: return 6; # 5 of a kind
                case 4: if (NBJ>0) return 6; else return 5; # 4 of a kind
                case 3: if (length(SORTEDCARD)==2) # Full house
                                if (NBJ>0) return 6; else return 4;
                        else # 3 of a kind
                                if (NBJ>0) return 5; else return 3;
                case 2: if (length(SORTEDCARD)==3) { # Double pairs
                                switch (NBJ) {
                                        case 2: return 5; # 4 of a kind
                                        case 1: return 4; # Full house
                                        case 0: return 2; # Double pair
                                        default: print "IMPOSSIBLE!"
                                }
                        }
                        else # Single pair
                                if (NBJ>0) return 3; else return 1;
                case 1: if (NBJ>0) return 1; else return 0;
                default: print "IMPOSSIBLE!"
        }
}
 

# First puzzle

```
cat input.txt | awk -v FS="" '{ for (i=1;i<=NF;i++) if (i <= NF/2) S[$i]=1; else if (S[$i]==1) {print $i; delete S; break} }' | tr -d $'\n' | od -An -tu1 | tr ' ' $'\n' | grep . | awk '{if ($1 > 95) S += $1-96; else S += $1-38} END { print S}'
```

Not overly proud of this one, except maybe for the first awk :-) It considers each letter as a field (`FS=""`) and then stores the existence of each letter in S, then prints the letter if it's in the second part.

The rest is just fluff: 

* tr to remove the \n
* od to print the ASCII code
* tr again to add the \n again
* grep to remove the empty lines
* awk to compute and add priority

# Second puzzle

```
cat input.txt | awk -v FS="" '{ ELF=NR%3; for (i=1;i<=NF;i++) {O[$i]=1; S[ELF,$i]=1}; if (ELF==0) { for (L in O) if (S[0,L]==1 && S[1,L]==1 && S[2,L]==1)  {print L; delete S; delete O; break}}}'| tr -d $'\n' | od -An -tu1 | tr ' ' $'\n' | grep . | awk '{if ($1 > 95) S += $1-96; else S += $1-38} END { print S}'
```

Yeah, OK, this is getting a bit too much maybe?    
awk stores all letters in O and the existence of each letter in a 3-line array S. Then, every 3 lines, it loops over the letters in O and checks in S if it was there on the 3 lines. The rest of the fluff is the same as above.
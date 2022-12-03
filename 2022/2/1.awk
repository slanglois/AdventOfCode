BEGIN {
  S["A"]=1; S["B"]=2; S["C"]=3;
  S["X"]=1; S["Y"]=2; S["Z"]=3;
}

{
  SCORE+=S[$2];
  if (S[$1]==S[$2]) SCORE+=3;
  if ((S[$1]+1)%3==S[$2]%3) SCORE+=6;
}

END {
  print SCORE
}

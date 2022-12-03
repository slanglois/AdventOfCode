BEGIN {
  S["A"]=1; S["B"]=2; S["C"]=3;
  S["X"]=1; S["Y"]=2; S["Z"]=3;
}

{
  if ($2=="Y") SCORE += 3+S[$1];
  if ($2=="X") SCORE += $1=="A"?3:S[$1]-1;
  if ($2=="Z") SCORE += ($1=="C"?1:S[$1]+1)+6;
}

END {
  print SCORE
}

BEGIN { POS=50 }
{
	DELTA=substr($1,2)
	if (substr($1,1,1)=="L") DELTA=-DELTA
	POS=(POS+DELTA+100)%100
	if (POS==0) PWD++
	print POS,PWD
}

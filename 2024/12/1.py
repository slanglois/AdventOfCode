import fileinput

A=[]
for line in fileinput.input():
	A.append(list(line.strip()))
MAXL=len(A)
MAXM=len(A[0])
print(MAXM,MAXL)

def colour_area(c, l: int, m: int) -> (int,int):
	print(c,l,m,A[l][m])
	s=1
	p=0
	A[l][m]=c.lower()
	# East
	if m<MAXM-1:
		if A[l][m+1]==c:
			(s1,p1)=colour_area(c,l,m+1)
			s+=s1
			p+=p1
		else:
			if A[l][m+1]!=c.lower(): p+=1
	else: p+=1
	# South
	if l<MAXL-1:
		if A[l+1][m]==c:
			(s1,p1)=colour_area(c,l+1,m)
			s+=s1
			p+=p1
		else:
			if A[l+1][m]!=c.lower(): p+=1
	else: p+=1
	# West
	if m>1:
		if A[l][m-1]==c:
			(s1,p1)=colour_area(c,l,m-1)
			s+=s1
			p+=p1
		else:
			if A[l][m-1]!=c.lower(): p+=1
	else: p+=1
	# North
	if l>1:
		if A[l-1][m]==c:
			(s1,p1)=colour_area(c,l-1,m)
			s+=s1
			p+=p1
		else:
			if A[l-1][m]!=c.lower(): p+=1
	else: p+=1
	return (s,p)

for l in range(MAXL):
	for m in range(MAXM):
		if A[l][m] != A[l][m].lower():
			c=A[l][m]
			print(c,colour_area(c,l,m))

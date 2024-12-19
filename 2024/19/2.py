import fileinput

# For better perf, store in how many ways a pattern is doable
DOABLE=dict()

def computepatterns(_pattern:str)->int:
    if _pattern=="": return 1
    if DOABLE.get(_pattern,None)!=None: return DOABLE[_pattern]
    NB=0
    for t in T:
        if _pattern.startswith(t):
            #print("  Try",t,"for",_pattern)
            NB+=computepatterns(_pattern[len(t):])
    DOABLE[_pattern]=NB
    return NB


S=0
for line in fileinput.input():
    if fileinput.lineno()==1:
        # Store available towels in a list
        T=list(line[:-1].split(", "))
        print(T)
    elif len(line)>1:
        S+=computepatterns(line[:-1])
        print(S,line)

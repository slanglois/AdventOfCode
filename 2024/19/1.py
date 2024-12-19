import fileinput

# For better perf, store if a pattern is doable or not
DOABLE=dict()

def isdoable(_pattern:str)->bool:
    if _pattern=="": return True
    if DOABLE.get(_pattern,None)!=None: return DOABLE[_pattern]
    for t in T:
        if _pattern.startswith(t):
            print("  Try",t,"for",_pattern)
            if isdoable(_pattern[len(t):]):
                DOABLE[_pattern]=True
                return True
    DOABLE[_pattern]=False
    return False


S=0
for line in fileinput.input():
    if fileinput.lineno()==1:
        # Store available towels in a list
        T=list(line[:-1].split(", "))
        print(T)
    elif len(line)>1:
        if isdoable(line[:-1]):
            S+=1
        print(S,line)

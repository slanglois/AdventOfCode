import fileinput

# Store all the page order constraints in a set
CONSTRAINTS=set()
S=0
for line in fileinput.input():
    if '|' in line:
        CONSTRAINTS.add(line[:-1])
    elif ',' in line:
        PAGES=line[:-1].split(',')
        print(PAGES)
        REORDERED=False
        i=0
        while i<len(PAGES)-1:
            if PAGES[i+1]+'|'+PAGES[i] in CONSTRAINTS:
                # A constraint is broken - swap the 2 elements and start again
                PAGES[i],PAGES[i+1]=PAGES[i+1],PAGES[i]
                print(PAGES,i,i+1)
                i=0
                REORDERED=True
            else: i+=1
        # Sum the middle element
        if REORDERED:
            S+=int(PAGES[(len(PAGES)-1)//2])
            print(S)

import fileinput

# Store all the page order constraints in a set
CONSTRAINTS=set()
S=0
for line in fileinput.input():
    if '|' in line:
        CONSTRAINTS.add(line[:-1])
    elif ',' in line:
        PAGES=line[:-1].split(',')
        for i in range(len(PAGES)-1):
            MIDPAGE=0
            if PAGES[i+1]+'|'+PAGES[i] in CONSTRAINTS:
                # A constraint is broken - stopping there
                print(PAGES,PAGES[i],i,S)
                break
            # We found the middle page!
            if i==(len(PAGES)-1)/2: MIDPAGE=PAGES[i]
            # If we reached that point, the line is good
            S+=int(MIDPAGE)
            print(PAGES,i,MIDPAGE,S)

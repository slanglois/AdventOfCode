import fileinput

line=fileinput.input().readline()
FILEID=0
ISFILE=True
DISK=[]
# Build the disk
for C in line[:-1]:
    for i in range(int(C)):
        if ISFILE:
            DISK.append(FILEID) 
        else:
            DISK.append(-1)
    if ISFILE: FILEID+=1
    ISFILE=not ISFILE
    #print(DISK)

I1=0
I2=len(DISK)-1
while I1<I2:
    # Look for the next empty space at the beginning
    while DISK[I1]!=-1: I1+=1
    # Look for the next non-empty space at the end
    while DISK[I2]==-1: I2-=1
    DISK[I1]=DISK[I2]
    DISK[I2]=-1
#    print("I1",I1,"I2",I2,DISK)
    I1+=1
    I2-=1

# Compute the checksum!
S=0
for i in range(I2+1):
    S+=i*DISK[i]
    print(i,DISK[i],S)
print(S)

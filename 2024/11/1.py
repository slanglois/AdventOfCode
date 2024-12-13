import fileinput

for line in fileinput.input():
    A=list(map(int,list(line.split(' '))))

print(A)

MAX=0
for count in range(25):
    B=[]
    for i in A:
        if i==0: B.append(1)
        # 0 -> 1
        elif len(str(i))%2 == 0:
        # even number of digits -> split in 2
            digits=len(str(i))//2 
            B.append(int(str(i)[0:digits]))
            B.append(int(str(i)[digits:]))
        else:
        # multiply by 2024 - and keep track of the max
            j=i*2024
            B.append(j)
            if j>MAX: MAX=j
    A=B
    print(MAX, len(A))

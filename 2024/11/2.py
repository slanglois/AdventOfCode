import fileinput

# We actually don't care about the order, so… let's just count how many of each stones there are!
S=dict()
def addStones(_K:dict, _i:int, _n:int):
    _K[_i]=_K.get(_i,0)+_n

for line in fileinput.input():
    for i in list(map(int,list(line.split(' ')))):
        addStones(S,i,1)
print(S)

for count in range(75):
    K=dict()
    for i in S:
        n=S[i]
        # 0 -> 1
        if i==0:
            addStones(K,1,n)
        elif len(str(i))%2 == 0:
        # even number of digits -> split in 2
            digits=len(str(i))//2 
            addStones(K,int(str(i)[0:digits]),n)
            addStones(K,int(str(i)[digits:]),n)
        else:
        # multiply by 2024
            addStones(K,i*2024,n)
    S=K
    SUM=0
    for j in S: SUM+=S[j]
    print(S,SUM)

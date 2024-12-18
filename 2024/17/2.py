import fileinput

for line in fileinput.input():
  if line.startswith("Register A"):
    A=int(line[12:])
  elif line.startswith("Register B"):
    B=int(line[12:])
  elif line.startswith("Register C"):
    C=int(line[12:])
  elif line.startswith("Program"):
    PROG=list(map(int,line[9:-1].split(',')))

print(A,B,C,PROG)

def comboperand(n:int) -> int:
  if 0<=n<4: return n
  elif n==4: return A
  elif n==5: return B
  elif n==6: return C
  else:
    print("WTF?",n)
    exit(12)

PREVN=1
N=2991328
OUTPUT=[]
while PROG != OUTPUT:
  # The programs producing an output that starts with the same few digits as the input
  # seem to happen at regular intervals of 4194304. (This number is also 2^24.)
  # That's probably not a coincidence, so lets try skipping by this amount :-) 
  N+=4194304
  A=N
  IP=0
  OUTPUT=[]
  while IP<len(PROG):
    match PROG[IP]:
      case 0:
        A=A//2**comboperand(PROG[IP+1])
        IP+=2
        #print("adv",A,IP)
      case 1:
        B^=PROG[IP+1]
        IP+=2
        #print("bxl",B,IP)
      case 2:
        B=comboperand(PROG[IP+1])%8
        IP+=2
        #print("bst",B,IP)
      case 3:
        if A==0: IP+=2
        else: IP=PROG[IP+1]
        #print("jnz",B,IP)
      case 4:
        B^=C
        IP+=2
        #print("bxc",B,IP)
      case 5:
        OUTPUT.append(comboperand(PROG[IP+1])%8)
        IP+=2
        #print("out",OUTPUT[-1],IP)
      case 6:
        B=A//2**comboperand(PROG[IP+1])
        IP+=2
        #print("bdv",B,IP)
      case 7:
        C=A//2**comboperand(PROG[IP+1])
        IP+=2
        #print("cdv",C,IP)
  if OUTPUT[0:12]==PROG[0:12]:
      print(N,N-PREVN,OUTPUT)
      PREVN=N

print(N,OUTPUT)

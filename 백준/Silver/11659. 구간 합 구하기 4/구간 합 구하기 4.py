import sys
i,n=map(int,sys.stdin.readline().strip().split())
numbers=list(map(int,sys.stdin.readline().strip().split()))
partialsum=[0 for _ in range(i)]
for cnt in range(i):
    if cnt==0:
        partialsum[cnt]=numbers[cnt]
    else:
        partialsum[cnt]=partialsum[cnt-1]+numbers[cnt]

def partialsumfunc(partialsum,start,end):
    if start-2<0:
        return partialsum[end-1]
    else:
        return partialsum[end-1]-partialsum[start-2]
    
for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    sys.stdout.write(str(partialsumfunc(partialsum,a,b))+'\n')
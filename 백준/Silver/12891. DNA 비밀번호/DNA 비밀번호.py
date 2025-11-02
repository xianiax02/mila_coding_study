import sys
#input=sys.stdin.readline
dnalength,codelength=map(int,input().strip().split())
dna=list(input().strip())
req=list(map(int,input().strip().split()))

cnt=0
codecount=[0,0,0,0] #ACGT
codetrans={'A':0,'C':1,'G':2,'T':3}
for i in range(codelength):
    codecount[codetrans[dna[i]]]+=1

p1,p2=0,(codelength-1)
while p2<dnalength:
    check=1
    for i in range(4):
        if codecount[i]<req[i]:
            check*=0
    if check:
        cnt+=1
    codecount[codetrans[dna[p1]]]-=1
    p1+=1
    p2+=1
    if not p2<dnalength:
        continue
    codecount[codetrans[dna[p2]]]+=1
sys.stdout.write(str(cnt))
            
        
        

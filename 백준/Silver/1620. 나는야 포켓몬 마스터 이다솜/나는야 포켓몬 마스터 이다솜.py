import sys
numdict=[]
namedict={}
n,m=list(map(int,(sys.stdin.readline().strip().split(' '))))

for i in range(1,n+1):
    data=sys.stdin.readline().strip()
    numdict.append(data)
    namedict[data]=i

for j in range(m):
    data=sys.stdin.readline().strip()
    if data.isdigit():
        datanum=int(data)
        sys.stdout.write(numdict[datanum-1]+'\n')
    else:
        sys.stdout.write(str(namedict[data])+'\n')
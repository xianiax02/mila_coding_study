import sys
deck={}
n=int(sys.stdin.readline().strip())
numlist=list(map(int,sys.stdin.readline().strip().split(' ')))
for num in numlist:
    if num in deck:
        deck[num]+=1
    else:
        deck[num]=1

m=int(sys.stdin.readline().strip())
checknumlist=list(map(int,sys.stdin.readline().strip().split(' ')))
for checknum in checknumlist:
    if checknum in deck:
        sys.stdout.write(str(deck[checknum])+' ')
    else:
        sys.stdout.write('0 ')
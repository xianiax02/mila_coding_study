import sys
from collections import Counter

n=int(sys.stdin.readline().strip())
numlist=list(map(int,sys.stdin.readline().strip().split(' ')))
deck=Counter(numlist)


m=int(sys.stdin.readline().strip())
checknumlist=list(map(int,sys.stdin.readline().strip().split(' ')))
result=[]
for checknum in checknumlist:
	result.append(str(deck[checknum]))    

print(' '.join(result))
n=int(input())
numlist=set(map(int,input().split(" ")))
m=int(input())
checklist=list(map(int,input().split(" ")))
for i in range(m):
	if checklist[i] in numlist:
		print(1)
	else:
		print(0)
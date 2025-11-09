import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
a=[]
for i in range(n):
    a.append((int(input().strip()),i))

b=sorted(a)
indexdiff=0
for i in range(n):
    indexdiff=max(b[i][1]-i,indexdiff)

print(str(indexdiff+1))
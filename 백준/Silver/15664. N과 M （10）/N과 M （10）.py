import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
n=len(numbers)
numbers.sort()
numset=set()
def search(x,step,lst):
    if step==m:
        numset.add(tuple([numbers[i] for i in lst]))
        return
    for nxt in range(x+1,n):
        search(nxt,step+1,lst+[nxt])

search(-1,0,[])
numset=sorted(list(numset))
for number in numset:
    print(' '.join(map(str,number)))

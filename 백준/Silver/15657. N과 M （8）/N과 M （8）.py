import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
def search(x,step,lst):
    if step==m:
        print(*[numbers[i] for i in lst])
        return
    for nxt in range(x,n):
        lst.append(nxt)
        search(nxt,step+1,lst)
        lst.pop()

search(0,0,[])
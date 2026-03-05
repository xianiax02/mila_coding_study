import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=[0]+list(map(int,input().split()))
numbers.sort()
visited=[False]*(n+1)
def search(x,step,lst):
    visited[x]=True
    if step==m:
        print(*[numbers[i] for i in lst])
    else:
        for nxt in range(x+1,n+1):
            if not visited[nxt]:
                search(nxt,step+1,lst+[nxt])
    visited[x]=False

search(0,0,[])
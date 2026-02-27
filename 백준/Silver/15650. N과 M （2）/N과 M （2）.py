n,m=map(int,input().split())
visited=[False]*(n+1)
lst=[]
def search(v,step):
    lst.append(v)
    if step==m:
        print(*lst)
    else:
        for i in range(v+1,n+1):
            search(i,step+1)
    if lst:
        lst.pop()

for i in range(1,n+1):
    search(i,1)
    
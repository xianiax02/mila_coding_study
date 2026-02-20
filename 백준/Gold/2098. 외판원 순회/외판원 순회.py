import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
wm=[]
inf=float('inf')
d=[[-1]*(n) for _ in range(2**n)]
for _ in range(n):
    wm.append(list(map(int,input().split())))

start=0 #0노드에서 출발
def dfs(state,current):
    if state==2**n-1:
        return wm[current][0] if wm[current][0] else inf
    if d[state][current]!=-1: #만약 채우져있으면 반환
        return d[state][current]
    tmp=inf
    for j in range(n):
        if wm[current][j] and not state&(1<<j): #안채워진 j와 연결된 j에 대해서 모든 j를 돌아보며 state,current 값을 채워감.
            tmp=min(dfs(state|1<<j,j)+wm[current][j],tmp)
    d[state][current]=tmp
    return d[state][current ]

answer=dfs(1,0)
print(answer)
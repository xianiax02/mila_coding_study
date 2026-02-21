import sys
input=sys.stdin.readline
commands=list(map(int,input().split()))
del commands[-1]
d={(0,0):0}
cost=[[1,2,2,2,2],
      [0,1,3,4,3],
      [0,3,1,3,4],
      [0,4,3,1,3],
      [0,3,4,3,1]]
inf=float('inf')
for step in commands:
    new_d=dict()
    for state,v in d.items():
       l=state[0]
       r=state[1]
       if step in state:
           new_d[state]=min(v+1,new_d.get(state,inf))
       else:
           new_d[(step,r)]=min(v+cost[l][step],new_d.get((step,r),inf))
           new_d[(l,step)]=min(v+cost[r][step],new_d.get((l,step),inf))
    d=new_d
answer=min(list(d.values()))
print(answer)
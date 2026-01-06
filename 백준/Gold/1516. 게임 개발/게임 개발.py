from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write
mq=deque()
n=int(input())
required=[0]*(n+1)
indegree=[0]*(n+1) #0-padding
graph=[[] for _ in range(n)]
graph.insert(0,0) #0-padding
ans=[0]*(1+n)
for target in range(1,n+1):
    command=list(map(int,input().split()))
    del command[-1] #마지막 -1원소 삭제
    required[target]=command[0]
    if len(command)>1:
        for pre in command[1:]:
            graph[pre].append(target) #pre->target 임을 저장
            indegree[target]+=1

for i in range(1,n+1):
    if indegree[i]==0:
        mq.append(i)
#각 건물을 동시에 짓는 것 -> 진입 차수가 0인 건물을 차례대로 짓는 것.-> 진입차수가 0인건물부터 체크, 근데 이제 그 중에서도 건설시간 짧은걸 먼저?
#그냥 진입 차수 0이면 지으면 되나? 상관없나? 어차피 진입차수 0인 건물들은 동시에 지어질 수 있음. 즉 상관 x
while mq:
    currentbuilding=mq.popleft()
    ans[currentbuilding]+=required[currentbuilding]
    for nextbuilding in graph[currentbuilding]:
        indegree[nextbuilding]-=1
        #ans[nextbuilding]+=required[currentbuilding] #필요로 하는 건물이 서로 우열이 있을 때만 적용 가능. 만약 상관없는 동시 건축 가능한 건물이라면 이는 성립하지 않음
        ans[nextbuilding]=max(ans[nextbuilding],ans[currentbuilding]) #ans currentbuilding 은 현재건물을 완성하는데 필요한 최소시간이 저장되어있음
        #간단히 말해서 한 건물 에 여러개의 건물이 필요할때, 그 건물이 사전에 필요한건 가장 시간이 오래걸리는 건물 하나라고 볼 수 있음.
        #지금은 사전준비 시간 미리 설정하는 거고, popleft할떄 본연의 건설시간 더하는 것임.
        #완성된 지금 건물의 시간과, 기존에 있던 다음 건물의 사전 준비시간을 비교해서 더 큰 사전 준비시간으로 갱신
        if indegree[nextbuilding]==0:
            mq.append(nextbuilding)
            
for i in range(1,n+1): #이러면 첫 원소 삭제할 필요 없음
    print(str(ans[i])+'\n')#join str만 받을 수 있음
            
    
    

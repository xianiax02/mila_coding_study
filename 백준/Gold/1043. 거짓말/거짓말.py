import sys
input=sys.stdin.readline
n,m=map(int,input().split())
people=[i for i in range(n+1)] #전체 수에 1개 추가 0-padding
truth=list(map(int,input().split())) #첫번째 원소는 진실 아는 사람 수
partylog=[]
def find(x):
    if people[x]==x:
        return x
    people[x]=find(people[x])
    return people[x] #처음에 x로 놓아버림

def union(unionlist):
    a=find(unionlist[0]) #첫번째 사람과 이후사람을 모두 union 연산
    for i in range(1,len(unionlist)):
        b=find(unionlist[i])
        if a!=b:
            people[max(a,b)]=min(a,b) #큰거가 작은거에 맞춤
        a=min(a,b) #a도 같이 업데이트 해줘야 이후의 노드가 통틀어서 사장 작은 노드를 기준으로 합쳐짐


#최종 결과 거짓말해서는 안되는 파티==truth 원소가 속한 root 0번째 사람은 제외 주의
if truth[0]==0: #진실 아는 사람이없을때
    print(m)
else:
    #맨처음에 진실 아는 사람들끼리 union 한번 해야함 --> 같은 조인걸로 간주할 수 있으니 지금 코드에서는 첫번째 진실아는 사람과 같은 조인게 중요
    cnt=m
    union(truth[1:])
    
    for _ in range(m):
        command=list(map(int,input().split()))
        unionlist=command[1:]
        union(unionlist)
        currentgroup=find(unionlist[0]) #지금 모임 첫번째 참가자기준으로 읽어서 noliegroup과 다르면 카운트 --> 근데 최종 결과를 기준으로 산정해야함.
        partylog.append(unionlist)
        #검사하는 시점이 다름 --> 각 모임별 정보를 저장하고 나중에 검사할 필요가 있음. 어차피 모임 최대 50 각 모임 최대 50명 2500크기 배열
    
    
    noliegroup=find(truth[1]) #root node를 찾을때는 반드시 find을 거쳐야함.   
    for i in range(m):
        '''
        if people[partylog[i][0]]==noliegroup:
            cnt-=1
            '''
        for member in partylog[i]:
            root=find(member)
            if root==noliegroup:
                cnt-=1
                break

    print(str(cnt))
    


        
    
from collections import deque
def solution(n, k, cmd):
    deleted=deque()
    is_deleted=[False]*n
    prev=[i-1 for i in range(n)] #prev[0]=-1
    post=[i+1 for i in range(n)] #prev[n-1]=n
    answer = ''
    def execute(command):
        nonlocal k
        if command[0]=='U':
            _,num=command.split()
            num=int(num)
            cnt=0
            for _ in range(num):
                k=prev[k]
        elif command[0]=='D':
            _,num=command.split()
            num=int(num)
            cnt=0
            for _ in range(num):
                k=post[k]
        elif command[0]=='C':
            is_deleted[k]=True
            deleted.append(k)
            temp=k
            if post[k]==n: #마지막이 삭제 되었다면
                k=prev[k]
                post[prev[temp]]=post[temp]
            elif prev[k]==-1: # 그게 아니라면 밑 칸으로 
                k=post[k]
                prev[post[temp]]=prev[temp]     
            else:
                k=post[k]
                post[prev[temp]]=post[temp]
                prev[post[temp]]=prev[temp]
        elif command[0]=='Z':
            last_deleted=deleted.pop()
            is_deleted[last_deleted]=False
            if prev[last_deleted]!=-1:
                post[prev[last_deleted]]=last_deleted
            if post[last_deleted]!=n:
                prev[post[last_deleted]]=last_deleted
    for command in cmd:
        execute(command)
    for val in is_deleted:
        if val:
            answer+='X'
        else:
            answer+='O'   
    return answer
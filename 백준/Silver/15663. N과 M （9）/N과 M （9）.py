def combination(sequence,visited,M,N):
    if len(sequence)==M:
        print(' '.join(map(str,sequence)))
        return
    for i in range(N):
        if i>0 and numlist[i]==numlist[i-1] and not visited[i-1]:
            continue
        if not visited[i]:
            visited[i]=True
            sequence.append(numlist[i])
            combination(sequence,visited,M,N)
            sequence.pop()
            visited[i]=False
    



N,M=list(map(int,input().split(' ')))
numlist=list(map(int,input().split(' ')))
numlist=sorted(numlist)
sequence=[]
visited=[False for _ in range(N)]
combination(sequence,visited,M,N)
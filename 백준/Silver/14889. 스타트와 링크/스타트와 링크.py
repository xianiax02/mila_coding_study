from itertools import combinations
N=int(input())
matrix=[]
for _ in range(N):
    row=list(map(int,input().split(' ')))
    matrix.append(row)

perteam=N//2
answer=99999
people=[i for i in range(N)]
candidates=list(combinations(people,perteam))
for start in candidates:
    link=list(filter(lambda x: x not in start,people))
    startstat=0
    linkstat=0
    for teammate,otherteammate in combinations(start,2):
        startstat+=matrix[teammate][otherteammate]
        startstat+=matrix[otherteammate][teammate]
    for teammate,otherteammate in combinations(link,2):
        linkstat+=matrix[teammate][otherteammate]
        linkstat+=matrix[otherteammate][teammate]
    difference=abs(startstat-linkstat)
    answer=min(answer,difference)

print(answer)
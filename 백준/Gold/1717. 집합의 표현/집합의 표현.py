import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
print=sys.stdout.write
n,m=map(int,input().split())
graph=[i for i in range(n+1)]
def union(a,b):
    global graph
    node1=a
    node2=b
    while graph[node1]!=node1 or graph[node2]!=node2:
        node1=graph[node1]
        node2=graph[node2]
    root=min(node1,node2) #치명적인 실수 root만 찾고 합치질 않음.
    graph[node1]=root
    graph[node2]=root    

nodea,nodeb=-1,-1
'''
def find(a,b):
    global graph
    global nodea,nodeb
    if graph[a]==a or graph[b]==b:
        nodea,nodeb=a,b
        return
    find(graph[a],graph[b])
    graph[a]=nodea
    graph[b]=nodeb
    '''
def find(a,b):
    global graph
    global nodea,nodeb
    if graph[a]==a and graph[b]==b:
        nodea,nodeb=a,b
        return
    find(graph[a],graph[b])
    graph[a]=nodea
    graph[b]=nodeb
for _ in range(m):
    o,a,b=map(int,input().split())
    if o==0:
        union(a,b)
    elif o==1:
        find(a,b)
        if graph[a]==graph[b]:
            print('YES\n')
        else:
            print('NO\n')
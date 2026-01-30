import sys
sys.setrecursionlimit(10**6)
def find_root(n, links,parent):
    for i in range(n):
        if links[i][0]!=-1:
            parent[links[i][0]]=i
        if links[i][1]!=-1:
            parent[links[i][1]]=i
    root_index=parent.index(-1)
    return root_index


            

def solution(k, num, links):
    answer = float('inf')
    n=len(num)
    parent=[-1]*(n)
    root=find_root(n,links,parent)
    def postorder(v,L,groupsize):
        nonlocal cnt
        r_sum,l_sum=0,0    
        if links[v][0]==-1 and links[v][1]==-1:
            groupsize[v]=num[v]
            return
        if links[v][0]!=-1:
            postorder(links[v][0],L,groupsize)
            l_sum=groupsize[links[v][0]]
        if links[v][1]!=-1:
            postorder(links[v][1],L,groupsize)
            r_sum=groupsize[links[v][1]]
        if l_sum+r_sum+num[v]>L:
            if l_sum>=r_sum and r_sum+num[v]<=L:
                groupsize[v]=r_sum+num[v]
                cnt+=1
            elif l_sum<r_sum and l_sum+num[v]<=L:
                groupsize[v]=l_sum+num[v]
                cnt+=1
            else:
                groupsize[v]=num[v]
                cnt+=2
        else:
            groupsize[v]=l_sum+r_sum+num[v]
            
    end=sum(num)
    start=max(num)
    while start<=end:
        L=(start+end)//2
        cnt=0
        groupsize=[0]*(n)
        postorder(root,L,groupsize)
        if cnt<k:
            answer=min(answer,max(groupsize))
            end=L-1
        else:
            start=L+1
    return answer
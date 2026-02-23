import sys
sys.setrecursionlimit(10**6)
def solution(info, edges):
    n=len(info)
    tree=[[] for _ in range(n)]
    for p,c in edges:
        tree[p].append(c)
    def postorder(node,wolves,sheep,candidates):
        nonlocal maxcount
        (wolves,sheep)=(wolves+1,sheep) if info[node] else (wolves,sheep+1)
        if wolves>=sheep:
            return 
        
        maxcount=max(maxcount,sheep)
        next_candidate=(candidates-{node})|set(tree[node]) #지금 노드는 합격이므로 자식노드만을 후보군에 넣는다. 
        for candidate in next_candidate:
            postorder(candidate,wolves,sheep,next_candidate)
    maxcount=0
    postorder(0,0,0,{0})
    return maxcount
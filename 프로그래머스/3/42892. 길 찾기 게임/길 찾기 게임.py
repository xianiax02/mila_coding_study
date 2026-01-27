import sys
sys.setrecursionlimit(10**6)
def preorder(node,tree,route1):

    if node==(0,-1,-1):
        return
    route1.append(node[0])
    preorder(tree[node][0],tree,route1)
    preorder(tree[node][1],tree,route1)
    
    
def postorder(node,tree,route2):
    if node==(0,-1,-1):
        return
    
    postorder(tree[node][0],tree,route2)
    postorder(tree[node][1],tree,route2)
    route2.append(node[0])
    
def solution(nodeinfo):
    newinfo=[]
    for i,node in enumerate(nodeinfo):
        newinfo.append((node[1],node[0],i+1))
    newinfo.sort(reverse=True)
    route1=[]
    route2=[]
    tree=dict()
    root=(newinfo[0][2],newinfo[0][1],newinfo[0][0]) #num,x,y
    tree[root]=[(0,-1,-1),(0,-1,-1)] #리프노드의 표기
    for (y,x,num) in newinfo:
        if num==root[0]:
            continue
        cnode=root
        temp=root
        while cnode!=(0,-1,-1): #지금 뽑은 노드보다 낮은 걸 확인 할 때 까지   
            temp=cnode
            if cnode[1]<x: #node는 오른쪽 아래로 가줘야함
                cnode=tree[cnode][1]
            else:
                cnode=tree[cnode][0]  
        if temp[1]<=x:
            tree[temp][1]=(num,x,y)
        else:
            tree[temp][0]=(num,x,y)
        tree[(num,x,y)]=[(0,-1,-1),(0,-1,-1)]
        
    preorder(root,tree,route1)
    postorder(root,tree,route2)
    answer = []
    answer.append(route1)
    answer.append(route2)
    
    return answer
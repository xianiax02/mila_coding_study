def solution(arrows):
    move={0:(0,1),1:(1,1),2:(1,0),3:(1,-1),4:(0,-1),5:(-1,-1),6:(-1,0),7:(-1,1)}
    traces=set()
    edges=set()
    cx,cy=0,0
    answer=0
    traces.add((cx,cy))
    for arrow in arrows:
        for _ in range(2):
            dx,dy=move[arrow] #직전 노드
            edge1=((cx,cy),(cx+dx,cy+dy))
            edge2=((cx+dx,cy+dy),(cx,cy))
            cx,cy=cx+dx,cy+dy
            if (cx,cy) in traces and (edge1 not in edges) and (edge2 not in edges):
                answer+=1
            traces.add((cx,cy))
            edges.add(edge1)
            edges.add(edge2)
    return answer
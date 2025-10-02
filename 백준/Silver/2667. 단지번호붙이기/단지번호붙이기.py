# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 13:31:36 2025

@author: wuchi
"""

import sys
from collections import deque
n=int(sys.stdin.readline().strip())
field=[]
visited=[[0]*n for _ in range(n)]
houses=[]
for _ in range(n):
    row=list(map(int,sys.stdin.readline().strip()))
    field.append(row)

def BFS(a,b,n,field,visited):
    queue=deque()
    cnt=0
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    queue.append((a,b))
    visited[b][a]=1
    cnt+=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<n) and (0<=ny<n):
                if field[ny][nx]==1 and visited[ny][nx]==0:
                    queue.append((nx,ny))
                    cnt+=1
                    visited[ny][nx]=1
    houses.append(cnt)
    return

for y in range(n):
    for x in range(n):
        if field[y][x]==1 and visited[y][x]==0:
            BFS(x,y,n,field,visited)

houses.sort() #caution
sys.stdout.write(str(len(houses))+'\n')
for i in houses:
    sys.stdout.write(str(i)+'\n')
        
    
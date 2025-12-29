import sys
from queue import PriorityQueue
input=sys.stdin.readline
n=int(input().strip())
numbers=[]
pq=PriorityQueue()
for i in range(n):
    pq.put(int(input().strip()))
    
ans=0    
while True:
    a=pq.get()
    if not pq.empty():
        b=pq.get()
        pq.put(a+b)
        ans+=a+b
    else:
        print(ans)
        break
    
    
    
    


#각 시점마다 병합 후에 기존 숫자 2개를 새로운 숫자 1개로 대체해서 가장 작은 숫자 2개를 더하게 해야하는데
#매번 정렬시키면 n^2logn이 됨. -> 시간 초과 
# 매번 정렬시키면 안됨. 이미 정렬되어있는거?이미 한번 정렬된 상태에서 시작할때,생각보다 넘어가는게 제한적임
#합쳐진 숫자를 정해진 위치에 집어넣는건 어떤가?
#-> 어떻게 구현할 것인가? 우선순위 큐!

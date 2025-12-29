import sys
import heapq
max_heap=[]
min_heap=[]
input=sys.stdin.readline
n=int(input())
#양수는 큰 순서대로 넣고 그 외는 작은순서대로 넣는다. 둘이 곱해서 기존 합보다 커지면 곱한값을 더하고 그게 아니면 각각 더한다. 
for i in range(n):
    num=int(input().strip())
    if num>0:
        heapq.heappush(max_heap,-num)
    else:
        heapq.heappush(min_heap,num)
ans=0
while max_heap:
    a=-1*heapq.heappop(max_heap)
    if max_heap: 
        b=-1*heapq.heappop(max_heap)
        if a*b > a+b:
            ans+=a*b
        else:
            ans+=a+b
        
    else:
        ans+=a
    
while min_heap:
    a=heapq.heappop(min_heap)
    if min_heap: 
        b=heapq.heappop(min_heap)
        if a*b > a+b:
            ans+=a*b
        else:
            ans+=a+b
    else:
        ans+=a

print(ans)
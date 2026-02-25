import sys
import heapq
input=sys.stdin.readline
print=sys.stdout.write
rxheap,lnheap=[],[]
n=int(input())
for _ in range(n):
    num=int(input())
    if lnheap and num<=lnheap[0]:
        heapq.heappush(rxheap,-num)
    elif rxheap and num>(-rxheap[0]):
        heapq.heappush(lnheap,num)
    else:
        heapq.heappush(rxheap,-num)
    while not (len(rxheap)==len(lnheap) or len(rxheap)==len(lnheap)+1):
        if len(rxheap)<len(lnheap):
            move=-heapq.heappop(lnheap)
            heapq.heappush(rxheap,move)
        else:
            move=-heapq.heappop(rxheap)
            heapq.heappush(lnheap,move)
    print(str(-rxheap[0])+'\n')

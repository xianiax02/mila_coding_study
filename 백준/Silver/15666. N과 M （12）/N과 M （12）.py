import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
numbers=sorted(list(set(numbers)))
n=len(numbers)
def search(x,step,lst):
    if step==m:
        print(*lst)
        return
    for nxt in range(x,n):
        lst.append(numbers[nxt])
        search(nxt,step+1,lst)
        lst.pop()
search(0,0,[])
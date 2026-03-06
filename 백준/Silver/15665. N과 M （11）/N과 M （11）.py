import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
numbers=sorted(list(set(numbers)))
n=len(numbers)
def search(step,lst):
    if step==m:
        print(*lst)
        return
    for nxt in range(n):
        lst.append(numbers[nxt])
        search(step+1,lst)
        lst.pop()
search(0,[])
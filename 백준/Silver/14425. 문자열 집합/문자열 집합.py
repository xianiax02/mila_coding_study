import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s=set()
for _ in range(n):
    word=input()
    s.add(word)
cnt=0
for _ in range(m):
    check=input()
    if check in s:
        cnt+=1

print(cnt)
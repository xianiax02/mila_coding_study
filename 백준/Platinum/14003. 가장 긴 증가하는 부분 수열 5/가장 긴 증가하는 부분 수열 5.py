from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
d=[0]*(n)
previndex=[-2]*n
tails_val = [a[0]]
tails_idx = [0]
d[0] = 1
result=[]
for i in range(1, n):
    # [수정 포인트] 안쪽 for j 루프 대신 bisect_left를 사용합니다.
    # a[i]가 들어갈 '길이(위치)'를 이진 탐색으로 0.00001초 만에 찾습니다.
    pos = bisect_left(tails_val, a[i])
    
    # 2. 내 앞에 올 놈의 인덱스를 기록 (이전 길이의 끝값 인덱스)
    if pos > 0:
        previndex[i] = tails_idx[pos - 1]
    
    # 3. 새로운 길이를 만들거나, 기존 길이를 더 작은 값으로 갱신
    if pos == len(tails_val):
        tails_val.append(a[i])
        tails_idx.append(i)
    else:
        tails_val[pos] = a[i]
        tails_idx[pos] = i
        
    d[i] = pos + 1

ans=max(d)
start=d.index(ans)
while start!=-2:
    result.append(str(a[start]))
    start=previndex[start] 
result.reverse()
print(ans) 
print(' '.join(result))   
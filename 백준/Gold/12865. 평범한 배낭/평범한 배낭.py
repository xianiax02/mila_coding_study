import sys
input=sys.stdin.readline
n,k=map(int,input().split())
things=[]
for _ in range(n):
    things.append(list(map(int,input().split())))
    
d = {0: 0}

for nw, nv in things:
    # 1. 루프 밖에서 이전 단계(d)를 통째로 복사해서 시작합니다.
    # 이렇게 하면 "물건을 넣지 않는 경우"가 이미 new_d에 모두 담깁니다.
    new_d = d.copy() 
    
    for w, v in d.items():
        if w + nw <= k:
            # 2. 물건을 넣는 경우만 계산해서 업데이트합니다.
            # 이미 new_d에 있는 값(이전 물건들로 만든 최선) vs 현재 물건을 추가한 값
            new_d[w + nw] = max(new_d.get(w + nw, 0), v + nv)
    
    d = new_d
answer=max([i for i in d.values()])
print(answer)

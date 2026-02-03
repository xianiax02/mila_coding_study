from bisect import bisect_left
#최대 제출 횟수+1=최대라운드 수=최대 쌍 개수+1
def solution(coin, cards):
    answer = 0
    n=len(cards)
    pointer=n//3
    pair=[0]*n
    used=[False]*n
    for i in range(n):
        pair[i]=cards.index(n+1-cards[i])
    for p in range(pointer+2,n+1,2):
        requiredcoin=float('inf')
        roundok=False
        #지금까지 뽑았던 수들 포함해서 cost 0으로 이번 라운드 넘길 수 있나?
        for i in range(pointer):
            if pair[i]<pointer and not used[i]:
                requiredcoin=0
                used[i]=True
                used[pair[i]]=True
                roundok=True
                break
        if not roundok:
            for i in range(pointer,p):
                if pair[i]<pointer and not used[i]:
                    requiredcoin=1
                    if coin>=1:
                        used[i]=True
                        used[pair[i]]=True
                        roundok=True
                        coin-=1
                        break
        if not roundok:
            for i in range(pointer,p):
                if pointer<=pair[i]<p and not used[i]:
                    requiredcoin=2
                    if coin>=2:
                        used[i]=True
                        used[pair[i]]=True
                        roundok=True
                        coin-=2
                        break
        if roundok:
            answer+=1
        else:
            break
    return answer+1
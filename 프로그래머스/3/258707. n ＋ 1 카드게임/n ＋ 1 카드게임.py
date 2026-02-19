import heapq
def solution(coin, cards):
    n=len(cards)
    rounds,pairs= 1,0
    chances=[]
    pset,aset=set(cards[:n//3]),set()
    def add_pair(i,j): #i인덱스부터 j인덱스까지 존재하는 모든 pair 을 cost와 함께 chances에 추가
        nonlocal pairs
        for idx in range(i,j+1):
            pair1,pair2=min(cards[idx],n+1-cards[idx]),max(cards[idx],n+1-cards[idx])
            if (pair1 in aset) and (pair2 in aset):
                 #내가 이미 있는 패는 pairs에 넣어서 집합연산에서 제외한다. 
                heapq.heappush(chances,(2,pair1,pair2))
                aset.discard(pair1)
                aset.discard(pair2)
            elif ((pair1 in aset) and (pair2 in pset)) or ((pair2 in aset) and (pair1 in pset)):
                heapq.heappush(chances,(1,pair1,pair2))
                aset.discard(pair1)
                aset.discard(pair2) #이미 넣은 pair는 더이상 검출 못하게.
            elif (pair1 in pset) and (pair2 in pset):
                pairs+=0.5
            else: continue
    add_pair(0,n//3-1)
    for idx in range(n//3,n,2):
        aset|=set(([cards[idx],cards[idx+1]]))
        add_pair(idx,idx+1)
        if pairs<1:
            if chances:
                cost,pair1,pair2=heapq.heappop(chances)
                if coin>=cost:
                    coin-=cost #pairs 1추가하고 바로 삭제하므로 pairs 조작 x
                    rounds+=1
                else:
                    return rounds
            else: return rounds
        else:
            pairs-=1
            rounds+=1
    return rounds
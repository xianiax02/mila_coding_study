import sys
input=sys.stdin.readline
n,blueraynum=map(int,input().split())
videos=list(map(int,input().split()))

def check(blueraysize):
    global videos,blueraynum,n
    cnt=1 #1부터 시작
    s=0
    for video in videos:
        if s+video>blueraysize:
            cnt+=1
            if cnt>blueraynum:
                return False
            s=video #비디오 하나가 사이즈 초과하는 경우도 처리 가능
        else:
            s+=video
    if cnt<=blueraynum:
        return True
    else:
        return False   

#average=totalvideos//n
# 숫자 너무 많으니까 전부 배열에 저장하는 게 아니라 그냥 인덱스를 숫자로 활용 blueraysizes=[i for i in range(max(videos),totalvideos+1)] 
start=max(videos)
end=sum(videos)
while start<=end:
    center=(start+end)//2
    if check(center): #다 넣어질때, 왼쪽으로 이동해본다.-->더 줄여볼 수 있음
        end=center-1
    else:
        start=center+1

print(start)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 1. 조합 테이블 구축 (N+M이 최대 200이므로 201까지)
MAX = N + M + 1
C = [[0] * MAX for _ in range(MAX)]

for i in range(MAX):
    C[i][0] = 1
    for j in range(1, i + 1):
        # K의 최대 범위(10억)를 고려해 상한선을 둡니다 (계산 효율성)
        C[i][j] = min(1000000007, C[i-1][j] + C[i-1][j-1])

# 2. 존재 가능한 범위인지 체크
if K > C[N + M][N]:
    print("-1")
else:
    result = []
    
    # wuchi님의 로직: a와 z가 모두 남아있는 동안 반복
    while N > 0 and M > 0:
        # 현재 자리에 'a'를 넣었을 때 나올 수 있는 경우의 수
        # 전체(N+M-1) 중 a(N-1)를 뽑는 경우
        count_if_a = C[N + M - 1][N - 1]
        
        if K <= count_if_a:
            # a를 고정해도 K번째가 그 범위 안에 있음 -> 'a' 추가
            result.append('a')
            N -= 1
        else:
            # a로 시작하는 그룹을 다 합쳐도 K에 못 미침 -> 'z' 추가
            result.append('z')
            K -= count_if_a  # 제쳐버린 'a' 그룹의 수만큼 K에서 차감
            M -= 1
            
    # 3. 루프 종료 후 남은 글자 처리 (a나 z 중 하나가 0이 되었을 때)
    result.extend(['a'] * N)
    result.extend(['z'] * M)
    
    print(''.join(result))
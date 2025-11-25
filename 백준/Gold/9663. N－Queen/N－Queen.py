import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

# 검사 속도를 O(1)로 만들기 위한 방문 체크 배열들
visited_col = [False] * n             # 열(Column) 체크
visited_diag1 = [False] * (2 * n)     # 대각선 / (row + col)
visited_diag2 = [False] * (2 * n)     # 대각선 \ (row - col + n - 1)

def Queen(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for col in range(n):
        # O(1) 검사: 열, 대각선1, 대각선2에 퀸이 없는지 확인
        if not visited_col[col] and \
           not visited_diag1[row + col] and \
           not visited_diag2[row - col + n - 1]:
            
            # 방문 처리
            visited_col[col] = True
            visited_diag1[row + col] = True
            visited_diag2[row - col + n - 1] = True
            
            Queen(row + 1)
            
            # 백트래킹 (방문 해제)
            visited_col[col] = False
            visited_diag1[row + col] = False
            visited_diag2[row - col + n - 1] = False

Queen(0)
print(cnt)
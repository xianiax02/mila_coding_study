import sys

def is_prime(n):
    """소수 판별 함수 (제곱근 최적화)"""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False # 짝수 제외 최적화
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """팰린드롬 판별 함수 (슬라이싱 활용)"""
    s = str(n)
    return s == s[::-1]

def solve():
    # 빠른 입력
    line = sys.stdin.readline().strip()
    if not line: return
    n = int(line)
    
    # 1,000,000 이상의 짝수 자릿수 팰린드롬은 소수가 될 수 없으므로 
    # n부터 1씩 증가시키며 조건에 맞는 수를 찾음
    target = n
    while True:
        # 팰린드롬 체크가 문자열 변환뿐이라 소수 판별보다 보통 빠름
        if is_palindrome(target):
            if is_prime(target):
                print(target)
                break
        target += 1

if __name__ == "__main__":
    solve()